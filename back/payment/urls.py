from django.urls import path

from .views import CoinView

app_name = "payment"

urlpatterns = [
    path("", CoinView.as_view()),
]
