from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import ValidationError


User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя"""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError({
                'errors': f"Имя '{value}' недопустимо",
            })
        return value


class CustomUserSerializer(UserSerializer):
    """ Сериализатор показа пользователя. """

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
        )
