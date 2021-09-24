import logging

from django.test import TestCase
from rest_framework.test import APIClient

from inventory.models import Beverage

logger = logging.getLogger(__name__)


class GetItemsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.path = "/inventory/"

    def test_get_beverages_then_success(self):
        # Creates 3 beverages.

        # Expected to have id = 1
        Beverage.objects.create(**{"name": "Pepsi", "value": "0.50", "quantity": 5})
        # Expected to have id = 2
        Beverage.objects.create(
            **{"name": "Sparkling Water", "value": "0.50", "quantity": 5}
        )
        # Expected to have id = 3
        Beverage.objects.create(**{"name": "Limol", "value": "0.50", "quantity": 5})

        response = self.client.generic(method="GET", path=self.path)
        assert response.status_code == 200
        assert response.data == [
            {"id": 1, "name": "Pepsi", "value": "0.50", "quantity": 5},
            {"id": 2, "name": "Sparkling Water", "value": "0.50", "quantity": 5},
            {"id": 3, "name": "Limol", "value": "0.50", "quantity": 5},
        ]

    def test_get_nothing_then_success(self):
        # No beverages created
        response = self.client.generic(method="GET", path=self.path)
        assert response.status_code == 200
        assert response.data == []
