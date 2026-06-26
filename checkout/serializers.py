from rest_framework import serializers

from .models import ShippingAddress


class CheckoutSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ShippingAddress

        exclude = (
            "user",
        )