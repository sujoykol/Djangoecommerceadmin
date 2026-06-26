from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import (
    RegisterSerializer,
    ProfileSerializer,
    ChangePasswordSerializer,
)


class RegisterView(
    generics.CreateAPIView
):
    serializer_class = RegisterSerializer


class ProfileView(
    generics.RetrieveUpdateAPIView
):

    serializer_class = ProfileSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.user


class ChangePasswordView(
    generics.UpdateAPIView
):

    serializer_class = ChangePasswordSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.user

    def update(
        self,
        request,
        *args,
        **kwargs
    ):

        user = self.get_object()

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        if not user.check_password(
            serializer.validated_data[
                "old_password"
            ]
        ):
            return Response(
                {
                    "error":
                    "Old password incorrect"
                },
                status=400
            )

        user.set_password(
            serializer.validated_data[
                "new_password"
            ]
        )

        user.save()

        return Response(
            {
                "message":
                "Password changed successfully"
            }
        )