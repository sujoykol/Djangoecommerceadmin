from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "full_name",
        "phone_number",
        "is_staff",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "full_name",
                    "phone_number",
                    "address",
                    "city",
                    "state",
                    "country",
                    "pincode",
                    "is_blocked",
                )
            },
        ),
    )