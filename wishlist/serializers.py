from rest_framework import serializers

from .models import Wishlist


class WishlistSerializer(
    serializers.ModelSerializer
):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = Wishlist
        fields = "__all__"