import json
import logging

from django.test import TestCase
from rest_framework.test import APIClient

from payment.models import Coin

logger = logging.getLogger(__name__)


class CoinViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.path = "/"

        self.coin = Coin.objects.create(
            **{"value": 0.25, "quantity": 0, "type": "QUARTER"}
        )

    def tearDown(self):
        self.coin.quantity = 0
        self.coin.save()

    def test_put_more_than_1_coin_then_error(self):
        # 2 coins
        data = {"coin": 2}
        assert self.coin.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.coin.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.coin.quantity == 0

        # 3 coins
        data = {"coin": 3}
        assert self.coin.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.coin.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.coin.quantity == 0

    def test_put_1_coin_then_success(self):
        data = {"coin": 1}
        assert self.coin.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.coin.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 1
        assert self.coin.quantity == 1

    def test_put_lower_than_1_coin_then_error(self):
        # 0 coin
        data = {"coin": 0}
        assert self.coin.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.coin.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.coin.quantity == 0

        # -1 coin (just for testing purposes)
        data = {"coin": -1}
        assert self.coin.quantity == 0
        response = self.client.generic(
            method="PUT",
            path=self.path,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.coin.refresh_from_db()
        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 0
        assert self.coin.quantity == 0
