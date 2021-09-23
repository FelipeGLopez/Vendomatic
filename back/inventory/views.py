import logging

from rest_framework import status, viewsets
from rest_framework.response import Response

from payment.models import Coin

from .models import Beverage
from .serializers import BeverageSerializer

logger = logging.getLogger(__name__)


class InventoryViewSet(viewsets.ViewSet):
    def list(self, request):
        beverages = Beverage.objects.filter(quantity__gt=0)
        serializer = BeverageSerializer(beverages, many=True)
        return Response(data=serializer.data)

    def update(self, request, pk=None):
        beverage = Beverage.objects.get(pk=pk)

        coin_type = Coin.CoinValues.QUARTER
        coin = Coin.objects.filter(type=coin_type).first()
        if beverage.quantity > 0:
            if beverage.value <= coin.quantity * coin.value:
                # Subtracts just 1 in quantity and returns that.
                beverage.quantity -= 1
                beverage.save()
                # Generic operation, but with the given requirements
                # ... it always will return 2.
                coin.quantity -= beverage.value // coin.value
                coin.save()

                return Response(
                    data={"quantity": 1},
                    headers={
                        "X-Coins": coin.quantity,
                        "X-Inventory-Remaining": beverage.quantity,
                    },
                )
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    headers={"X-Coins": coin.quantity},
                )
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND, headers={"X-Coins": coin.quantity}
            )
