import json
import logging

from django.test import TestCase
from rest_framework.test import APIClient

from payment.models import Coin

logger = logging.getLogger(__name__)


class CoinPutTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.path = "/"

        # Creates a quarter with quantity 0.
        self.quarter = Coin.objects.create(
            **{"value": 0.25, "quantity": 0, "type": "QUARTER"}
        )

    def tearDown(self):
        self.quarter.quantity = 0
        self.quarter.save()

    def test_put_more_than_one_coin_then_error(self):
        # 2 coins
        data = {"coin": 2}
        assert self.quarter.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.quarter.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.quarter.quantity == 0

        # 3 coins
        data = {"coin": 3}
        assert self.quarter.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.quarter.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.quarter.quantity == 0

    def test_put_one_coin_then_success(self):
        data = {"coin": 1}
        assert self.quarter.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.quarter.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 1
        assert self.quarter.quantity == 1

    def test_put_lower_than_one_coin_then_error(self):
        # 0 coin
        data = {"coin": 0}
        assert self.quarter.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.quarter.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.quarter.quantity == 0

        # -1 coin (just for testing purposes)
        data = {"coin": -1}
        assert self.quarter.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.quarter.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.quarter.quantity == 0

    def test_put_successive_coins_then_success(self):
        data = {"coin": 1}
        assert self.quarter.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.quarter.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 1
        assert self.quarter.quantity == 1
        # Instert another coin
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.quarter.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 2
        assert self.quarter.quantity == 2
