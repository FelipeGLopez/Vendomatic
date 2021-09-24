import logging

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Coin

logger = logging.getLogger(__name__)


class CoinView(APIView):
    def __init__(self):
        coin_type = Coin.CoinValues.QUARTER
        self.coin = Coin.objects.filter(type=coin_type).first()

    def put(self, request):
        coin_quantity = request.data.get("coin")
        if coin_quantity and 0 < coin_quantity <= settings.MAX_COINS_ALLOWED:
            self.coin.quantity += coin_quantity
            self.coin.save()
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                headers={"X-Coins": self.coin.quantity},
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST, headers={"X-Coins": self.coin.quantity}
        )

    def get(self, request):
        return Response({"quantity": self.coin.quantity})

    def delete(self, request):
        remaining_coins = self.coin.quantity
        self.coin.quantity = 0
        self.coin.save()
        return Response(
            status=status.HTTP_204_NO_CONTENT, headers={"X-Coins": remaining_coins}
        )
