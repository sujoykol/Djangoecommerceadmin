from django.contrib import admin

from .models import Order
from .models import OrderItem


class OrderItemInline(
    admin.TabularInline
):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [OrderItemInline]

    list_display = (
        "order_number",
        "user",
        "grand_total",
        "payment_status",
        "order_status",
        "created_at",
    )

    list_filter = (
        "payment_status",
        "order_status",
    )

    search_fields = (
        "order_number",
        "user__username",
    )

    list_editable = (
        "payment_status",
        "order_status",
    )