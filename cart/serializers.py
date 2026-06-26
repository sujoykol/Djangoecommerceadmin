from rest_framework import serializers

from .models import Cart
from .models import CartItem


class CartItemSerializer(
    serializers.ModelSerializer
):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_image = serializers.SerializerMethodField()

    price = serializers.ReadOnlyField()

    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = CartItem

        fields = [
            "id",
            "product",
            "product_name",
            "product_image",
            "quantity",
            "price",
            "subtotal",
        ]

    def get_product_image(
        self,
        obj
    ):

        image = obj.product.images.filter(
            is_primary=True
        ).first()

        if not image:
            image = obj.product.images.first()

        if image:

            request = self.context.get(
                "request"
            )

            if request:
                return request.build_absolute_uri(
                    image.image.url
                )

            return image.image.url

        return None


class CartSerializer(
    serializers.ModelSerializer
):

    items = CartItemSerializer(
        many=True,
        read_only=True
    )

    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart

        fields = [
            "id",
            "items",
            "total"
        ]

    def get_total(
        self,
        obj
    ):

        return sum(
            item.subtotal
            for item in obj.items.all()
        )

    def to_representation(
        self,
        instance
    ):

        data = super().to_representation(
            instance
        )

        data["items"] = CartItemSerializer(
            instance.items.all(),
            many=True,
            context=self.context
        ).data

        return data