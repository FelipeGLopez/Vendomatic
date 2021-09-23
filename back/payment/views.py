import logging

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Coin

logger = logging.getLogger(__name__)


class CoinView(APIView):
    def put(self, request):
        coin_quantity = request.data.get("coin")
        coin_type = Coin.CoinValues.QUARTER
        coin = Coin.objects.filter(type=coin_type).first()
        if coin_quantity and 0 < coin_quantity <= settings.MAX_COINS_ALLOWED:
            coin.quantity += coin_quantity
            coin.save()
            return Response(
                status=status.HTTP_204_NO_CONTENT, headers={"X-Coins": coin.quantity}
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST, headers={"X-Coins": coin.quantity}
        )

    def delete(self, request):
        coin_type = Coin.CoinValues.QUARTER
        coin = Coin.objects.filter(type=coin_type).first()
        remaining_coins = coin.quantity
        coin.quantity = 0
        coin.save()
        return Response(
            status=status.HTTP_204_NO_CONTENT, headers={"X-Coins": remaining_coins}
        )
