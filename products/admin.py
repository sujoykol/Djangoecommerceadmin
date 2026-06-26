from django.contrib import admin
from django.utils.html import format_html

from .models import Product
from .models import ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    inlines = [
        ProductImageInline
    ]

    list_display = (
        "id",
        "image_preview",
        "name",
        "category",
        "price",
        "stock",
        "featured",
        "status",
    )

    def image_preview(self, obj):

        image = obj.images.filter(
            is_primary=True
        ).first()

        if image:

            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px;" />',
                image.image.url
            )

        return "-"

    image_preview.short_description = "Image"