from django.contrib.auth.models import User

from core.serializers import DynamicFieldsModelSerializer


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email"
        )

