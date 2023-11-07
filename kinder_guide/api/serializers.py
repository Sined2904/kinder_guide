from comments.models import ReviewKindergarten, ReviewSchool
from education.models import (AgeCategory, Area, Favourites_School,
                              KindergartenAlbum, Kindergartens, Language,
                              Profile, School, SchoolAlbum, Underground,
                              Favourites_Kindergartens, Sport, Intelligence,
                              Music, Create)
from news.models import News

from rest_framework import serializers

from .utils import get_avg_rating, get_coordinates_from_address


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
        fields = ['name', 'slug']


class SportSerializer(serializers.ModelSerializer):
    """Сериализатор модели возрастной категории."""

    class Meta:
        model = Sport
        fields = ['name', 'slug']


class CreateSerializer(serializers.ModelSerializer):
    """Сериализатор модели возрастной категории."""

    class Meta:
        model = Create
        fields = ['name', 'slug']


class IntelligenceSerializer(serializers.ModelSerializer):
    """Сериализатор модели возрастной категории."""

    class Meta:
        model = Intelligence
        fields = ['name', 'slug']


class MusicSerializer(serializers.ModelSerializer):
    """Сериализатор модели возрастной категории."""

    class Meta:
        model = Music
        fields = ['name', 'slug']


class SchoolAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбома для школы."""

    image = serializers.ImageField()

    class Meta:
        model = SchoolAlbum
        fields = ['image', ]


class SchoolShortSerializer(serializers.ModelSerializer):
    """Сериализатор модели школы (кратко)."""

    album = SchoolAlbumSerializer(many=True)
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
                  'description', 'address', 'album',
                  'price', 'is_favorited']


class SchoolSerializer(serializers.ModelSerializer):
    """Сериализатор модели школы."""

    area = AreaSerializer()
    underground = UndergroundSerializer(many=True)
    languages = LanguageSerializer(many=True)
    profile = ProfileSerializer(many=True)
    album = SchoolAlbumSerializer(many=True)
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

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

    def get_coordinates(self, obj):
        return get_coordinates_from_address(School, obj)

    class Meta:
        model = School
        fields = ['id', 'name', 'rating', 'reviews',
                  'description', 'telephone', 'address',
                  'underground', 'area', 'email', 'website',
                  'album', 'price', 'price_of_year',
                  'classes', 'languages', 'profile',
                  'working_hours',
                  'is_favorited', 'coordinates']


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
    is_favorited = serializers.SerializerMethodField()
    album = KindergartenAlbumSerializer(many=True)

    def get_rating(self, obj):
        return get_avg_rating(ReviewKindergarten, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            return Favourites_Kindergartens.objects.filter(
                kindergartens=obj, user=user).exists()
        return False

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'rating', 'reviews',
                  'description', 'address', 'album', 'price',
                  'is_favorited']


class KindergartensSerializer(serializers.ModelSerializer):
    """Сериализатор модели детского сада."""

    area = AreaSerializer()
    underground = UndergroundSerializer(many=True)
    languages = LanguageSerializer(many=True)
    album = KindergartenAlbumSerializer(many=True)
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    age_category = AgeCategorySerializer(many=True)
    is_favorited = serializers.SerializerMethodField()
    sport_dev = SportSerializer(many=True)
    create_dev = CreateSerializer(many=True)
    music_dev = MusicSerializer(many=True)
    intel_dev = IntelligenceSerializer(many=True)
    coordinates = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return get_avg_rating(ReviewKindergarten, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            return Favourites_Kindergartens.objects.filter(
                kindergartens=obj, user=user).exists()
        return False

    def get_coordinates(self, obj):
        return get_coordinates_from_address(self, obj)

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'rating', 'reviews',
                  'album', 'description', 'telephone',
                  'address', 'price', 'price_of_year',
                  'email', 'website', 'underground', 'area',
                  'languages', 'working_hours',
                  'group_suze', 'sport_dev', 'create_dev',
                  'music_dev', 'intel_dev', 'age_category',
                  'is_favorited']


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор новостей."""

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'date_posted','image']
                  'is_favorited', 'coordinates', 'preparing_for_school']
