from django.contrib import admin

from .models import ShippingAddress


@admin.register(ShippingAddress)
class ShippingAddressAdmin(
    admin.ModelAdmin
):

    list_display = (
        "full_name",
        "phone",
        "city",
        "country",
        "created_at",
    )