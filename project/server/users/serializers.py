from django.contrib.auth import get_user_model, authenticate

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
            "id"
        )


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "token"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError(
                "Для входа требуется email, указанный при регистрации."
            )

        if password is None:
            raise serializers.ValidationError(
                "Для входа требуется пароль."
            )
        
        user = authenticate(username=email, password=password)

        if user in None:
            raise serializers.ValidationError(
                "Пользователь с указанными email и почтовым адресом не найден."
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                "Данная учётная запись не активна."
            )

        return {
            "email": user.email,
            "token": user.token
        }
