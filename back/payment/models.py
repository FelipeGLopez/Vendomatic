from django.db import models


class Coin(models.Model):
    """
    Generic model for coins
    """

    class CoinValues(models.TextChoices):
        QUARTER = "QUARTER"

    value = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    type = models.CharField(
        max_length=20,
        choices=CoinValues.choices,
        default=CoinValues.QUARTER,
    )
