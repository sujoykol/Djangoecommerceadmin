from rest_framework import serializers

from .models import Product
from .models import ProductImage


class ProductImageSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = ProductImage

        fields = [
            "id",
            "image",
            "is_primary"
        ]


class ProductSerializer(
    serializers.ModelSerializer
):

    images = ProductImageSerializer(
        many=True,
        read_only=True
    )

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:

        model = Product

        fields = "__all__"