from django.db import models


class Beverage(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
