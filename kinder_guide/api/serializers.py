from comments.models import ReviewKindergarten, ReviewSchool
from education.models import (AgeCategory, Area, Favourites_School,
                              KindergartenAlbum, Kindergartens, Language,
                              Profile, School, SchoolAlbum, Underground)
from rest_framework import serializers

from .utils import get_avg_rating


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзывов."""

    grade = serializers.IntegerField(source='rating')


class ReviewSchoolSerializer(ReviewSerializer):
    """Сериализатор отзывов школы."""

    class Meta:
        model = ReviewSchool
        fields = ['id', 'content', 'grade', 'author', 'date_posted']


class ReviewKindergartenSerializer(ReviewSerializer):
    """Сериализатор отзывов детского сада."""

    class Meta:
        model = ReviewKindergarten
        fields = ['id', 'content', 'grade', 'author', 'date_posted']


class AreaSerializer(serializers.ModelSerializer):
    """Сериализатор модели округа."""

    class Meta:
        model = Area
        fields = ['name', 'slug']


class UndergroundSerializer(serializers.ModelSerializer):
    """Сериализатор модели метро."""

    class Meta:
        model = Underground
        fields = ['name', 'slug']


class LanguageSerializer(serializers.ModelSerializer):
    """Сериализатор модели языков."""

    class Meta:
        model = Language
        fields = ['name', 'slug']


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор модели профилей."""

    class Meta:
        model = Profile
        fields = ['name', 'slug']


class AgeCategorySerializer(serializers.ModelSerializer):
    """Сериализатор модели возрастной категории."""

    class Meta:
        model = AgeCategory
        fields = ['category', ]


class SchoolAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбома для школы."""

    image = serializers.ImageField()

    class Meta:
        model = SchoolAlbum
        fields = ['image', ]


class SchoolShortSerializer(serializers.ModelSerializer):
    """Сериализатор модели школы (кратко)."""

    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return get_avg_rating(ReviewSchool, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = School
        fields = ['id', 'name', 'rating', 'reviews',
                  'description', 'address', 'album',
                  'price', 'is_favorited']


class SchoolSerializer(serializers.ModelSerializer):
    """Сериализатор модели школы."""

    area = AreaSerializer()
    underground = UndergroundSerializer(many=True)
    languages = LanguageSerializer(many=True)
    profile = ProfileSerializer(many=True)
    album = SchoolAlbumSerializer(many=True)
    age_category = AgeCategorySerializer()
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return get_avg_rating(ReviewSchool, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            return Favourites_School.objects.filter(
                school=obj, user=user).exists()
        return False

    class Meta:
        model = School
        fields = ['id', 'name', 'rating', 'reviews',
                  'description', 'telephone', 'address',
                  'underground', 'area', 'email', 'website',
                  'album', 'price', 'price_of_year', 'age',
                  'classes', 'languages', 'profile',
                  'working_hours', 'age_category',
                  'is_favorited']


class KindergartenAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбома для детского сада."""

    image = serializers.ImageField()

    class Meta:
        model = KindergartenAlbum
        fields = ['image', ]


class KindergartensShortSerializer(serializers.ModelSerializer):
    """Сериализатор модели детского сада (кратко)."""

    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return get_avg_rating(ReviewKindergarten, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'rating', 'reviews',
                  'description', 'address', 'album', 'price']


class KindergartensSerializer(serializers.ModelSerializer):
    """Сериализатор модели детского сада."""

    area = AreaSerializer()
    underground = UndergroundSerializer(many=True)
    languages = LanguageSerializer(many=True)
    album = KindergartenAlbumSerializer(many=True)
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    age_category = AgeCategorySerializer()

    def get_rating(self, obj):
        return get_avg_rating(ReviewKindergarten, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'rating', 'reviews',
                  'album', 'description', 'telephone',
                  'address', 'price', 'price_of_year',
                  'email', 'website', 'underground', 'area',
                  'languages', 'age', 'working_hours',
                  'group_suze', 'sport_dev', 'create_dev',
                  'music_dev', 'intel_dev', 'age_category']
