import logging

from django.test import TestCase
from rest_framework.test import APIClient

from inventory.models import Beverage
from payment.models import Coin

logger = logging.getLogger(__name__)


class BuyItemsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def path(self, id):
        return f"/inventory/{id}/"

    def loadBeverages(self):
        # Creates 3 beverages.

        # Expected to have id = 1
        Beverage.objects.create(**{"name": "Pepsi", "value": "0.50", "quantity": 5})
        # Expected to have id = 2
        Beverage.objects.create(
            **{"name": "Sparkling Water", "value": "0.50", "quantity": 5}
        )
        # Expected to have id = 3
        Beverage.objects.create(**{"name": "Limol", "value": "0.50", "quantity": 5})

    def loadQuarter(self, quantity):
        return Coin.objects.create(
            **{"value": "0.25", "quantity": quantity, "type": "QUARTER"}
        )

    def test_buy_one_beverage_then_success(self):
        self.loadBeverages()
        quarter = self.loadQuarter(5)
        beverage_id = 1
        response = self.client.generic(method="PUT", path=self.path(beverage_id))
        quarter.refresh_from_db()

        assert response.status_code == 200
        assert int(response.headers["X-Coins"]) == 3
        assert int(response.headers["X-Inventory-Remaining"]) == 4
        assert response.data["quantity"] == 1
        assert quarter.quantity == 3

    def test_buy_two_beverages_consecutively_then_success(self):
        self.loadBeverages()
        assert Beverage.objects.get(id=1).quantity == 5

        quarter = self.loadQuarter(5)
        beverage_id = 1
        response = self.client.generic(method="PUT", path=self.path(beverage_id))
        quarter.refresh_from_db()

        assert response.status_code == 200
        assert int(response.headers["X-Coins"]) == 3
        assert int(response.headers["X-Inventory-Remaining"]) == 4
        assert response.data["quantity"] == 1
        assert Beverage.objects.get(id=1).quantity == 4
        assert quarter.quantity == 3

        response = self.client.generic(method="PUT", path=self.path(beverage_id))
        quarter.refresh_from_db()

        assert response.status_code == 200
        assert int(response.headers["X-Coins"]) == 1
        assert int(response.headers["X-Inventory-Remaining"]) == 3
        assert response.data["quantity"] == 1
        assert Beverage.objects.get(id=1).quantity == 3
        assert quarter.quantity == 1

        return quarter, beverage_id

    def test_buy_two_items_and_then_not_enugh_for_third_item_then_error(self):
        quarter, beverage_id = self.test_buy_two_beverages_consecutively_then_success()
        response = self.client.generic(method="PUT", path=self.path(beverage_id))

        assert response.status_code == 400
        assert int(response.headers["X-Coins"]) == 1
        assert Beverage.objects.get(id=1).quantity == 3
        assert quarter.quantity == 1

    def test_buy_all_items_then_buy_another_then_error(self):
        self.loadBeverages()
        beverage_id = 1
        initial_quantity = 20
        quarter = self.loadQuarter(initial_quantity)  # Set quantity to 20

        # Buy the 5 items for id = 1
        for i in range(1, 6):
            response = self.client.generic(method="PUT", path=self.path(beverage_id))
            quarter.refresh_from_db()

            assert response.status_code == 200
            assert int(response.headers["X-Coins"]) == (initial_quantity - (i * 2))
            assert (
                int(response.headers["X-Inventory-Remaining"])
                == Beverage.objects.get(id=1).quantity
            )
            assert response.data["quantity"] == 1
            assert quarter.quantity == (initial_quantity - (i * 2))

        response = self.client.generic(method="PUT", path=self.path(beverage_id))
        quarter.refresh_from_db()

        assert response.status_code == 404
        assert int(response.headers["X-Coins"]) == (
            initial_quantity - (5 * 2)
        )  # Due to the 5 items
        assert quarter.quantity == (initial_quantity - (5 * 2))
