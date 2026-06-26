from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "full_name",
            "phone_number",
            "password",
            "password2",
        ]

    def validate(self, attrs):

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                "Passwords do not match."
            )

        validate_password(attrs["password"])

        return attrs

    def create(self, validated_data):

        validated_data.pop("password2")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            full_name=validated_data.get("full_name", ""),
            phone_number=validated_data.get("phone_number", ""),
            password=validated_data["password"],
        )

        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        exclude = [
            "password",
            "groups",
            "user_permissions"
        ]


class ChangePasswordSerializer(
    serializers.Serializer
):

    old_password = serializers.CharField()

    new_password = serializers.CharField()