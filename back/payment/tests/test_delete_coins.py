import logging

from django.test import TestCase
from rest_framework.test import APIClient

from payment.models import Coin

logger = logging.getLogger(__name__)


class CoinDeleteTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.path = "/"

        # Creates a quarter with quantity 3.
        self.coin = Coin.objects.create(
            **{"value": 0.25, "quantity": 3, "type": "QUARTER"}
        )

    def test_delete_coins_with_quantity_greater_than_0_then_success(self):
        assert self.coin.quantity == 3
        response = self.client.generic(method="DELETE", path=self.path)
        self.coin.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 3
        assert self.coin.quantity == 0

    def test_delete_coins_with_quantity_0_then_success(self):
        self.coin.quantity = 0
        self.coin.save()
        assert self.coin.quantity == 0
        response = self.client.generic(method="DELETE", path=self.path)
        self.coin.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 0
        assert self.coin.quantity == 0

    def test_delete_successively_then_success(self):
        assert self.coin.quantity == 3
        response = self.client.generic(method="DELETE", path=self.path)
        self.coin.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 3
        assert self.coin.quantity == 0
        response = self.client.generic(method="DELETE", path=self.path)
        self.coin.refresh_from_db()
        assert response.status_code == 204
        assert int(response.headers["X-Coins"]) == 0
        assert self.coin.quantity == 0
