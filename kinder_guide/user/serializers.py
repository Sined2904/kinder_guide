from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор показа пользователя."""

    class Meta:
        model = User
        fields = [
            'email',
            'phone',
            'first_name',
            'last_name',
            'child_first_name',
            'child_last_name',
        ]


class CusstomUserDeleteSerializer(serializers.Serializer):
    """Сериализатор удаления пользователя БЕЗ запроса пароля."""

    pass
