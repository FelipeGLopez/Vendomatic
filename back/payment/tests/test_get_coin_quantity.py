import logging

from django.test import TestCase
from rest_framework.test import APIClient

from payment.models import Coin

logger = logging.getLogger(__name__)


class GetItemsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.path = "/"

    def test_get_quarter_quantity_then_success(self):
        coin = Coin.objects.create(**{"value": 0.25, "quantity": 0, "type": "QUARTER"})
        response = self.client.generic(method="GET", path=self.path)
        assert response.status_code == 200
        assert response.data == {"quantity": 0}

        coin.quantity = 5
        coin.save()

        response = self.client.generic(method="GET", path=self.path)
        assert response.status_code == 200
        assert response.data == {"quantity": 5}
