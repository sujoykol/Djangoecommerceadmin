from django.db import models


class Banner(models.Model):

    title = models.CharField(max_length=255)

    subtitle = models.CharField(
        max_length=255,
        blank=True
    )

    image = models.ImageField(
        upload_to="banners/"
    )

    button_text = models.CharField(
        max_length=100,
        blank=True
    )

    button_link = models.CharField(
        max_length=255,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title