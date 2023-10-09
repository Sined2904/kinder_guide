from rest_framework import serializers

from education.models import Language, Profile, Education

class LanguageSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Language"""

    class Meta:
        fields = (
            'id',
            'name',
            'slug'
        )
        model = Language


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Profile"""

    class Meta:
        fields = (
            'id',
            'name',
            'slug'
        )
        model = Profile


class EducationReadSerializer(serializers.ModelSerializer):
    """Сериализатор модели Education на вывод"""
    languages = LanguageSerializer(
        many=True,
        read_only=True
    )
    profile = ProfileSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        fields = (
            'id',
            'name',
            'role',
            'description',
            'telephone',
            'address',
            'price',
            'age',
            'languages',
            'profile',
        )
        model = Education