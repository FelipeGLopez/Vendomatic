from rest_framework import serializers

from inventory.models import Beverage


class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = "__all__"
