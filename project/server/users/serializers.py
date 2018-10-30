from django.contrib.auth import get_user_model, authenticate

import jwt
from rest_framework import serializers

from core.serializers import DynamicFieldsModelSerializer

User = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )

        read_only_fields = (
            "id",
        )


class RegistrationSerializer(serializers.Serializer):
    pass


class LoginSerializer(serializers.Serializer):
    pass
