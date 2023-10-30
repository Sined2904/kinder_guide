from comments.models import ReviewCourse, ReviewKindergarten, ReviewSchool
from education.models import (AgeCategory, Album, Area, Course, Kindergartens,
                              Language, Profile, School, Underground)
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


class ReviewCourseSerializer(ReviewSerializer):
    """Сериализатор отзывов курса."""

    class Meta:
        model = ReviewCourse
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


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбома."""
    image = serializers.ImageField()

    class Meta:
        model = Album
        fields = ['image',]


class AgeCategorySerializer(serializers.ModelSerializer):
    """Сериализатор модели возрастной категории."""

    class Meta:
        model = AgeCategory
        fields = ['category',]


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
                  'description', 'album', 'price']


class SchoolSerializer(serializers.ModelSerializer):
    """Сериализатор модели школы."""
    area = AreaSerializer()
    underground = UndergroundSerializer(many=True)
    languages = LanguageSerializer(many=True)
    profile = ProfileSerializer(many=True)
    album = AlbumSerializer(many=True)
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    age_category = AgeCategorySerializer()

    def get_rating(self, obj):
        return get_avg_rating(ReviewSchool, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = School
        fields = ['id', 'name', 'rating', 'reviews',
                  'description', 'telephone', 'address',
                  'underground', 'area', 'email',
                  'album', 'price', 'price_of_year', 'age',
                  'classes', 'languages', 'profile',
                  'name_author', 'working_hours', 'age_category']


class FilterSchoolSerializer(serializers.ModelSerializer):
    """Сериализатор фильтров модели школы."""

    class Meta:
        model = School
        fields = ['profile', 'age_category', 'languages',
                  'underground', 'area', 'price',]


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
                  'description', 'album', 'price']


class KindergartensSerializer(serializers.ModelSerializer):
    """Сериализатор модели детского сада."""
    area = AreaSerializer()
    underground = UndergroundSerializer(many=True)
    languages = LanguageSerializer(many=True)
    album = AlbumSerializer(many=True)
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
                  'email', 'underground', 'area',
                  'languages', 'age', 'working_hours',
                  'group_suze', 'sport_dev', 'create_dev',
                  'music_dev', 'intel_dev', 'age_category']


class FilterKindergartenSerializer(serializers.ModelSerializer):
    """Сериализатор фильтров модели детского сада."""

    class Meta:
        model = Kindergartens
        fields = ['age_category', 'languages',
                  'underground', 'area', 'price',]


class CourseShortSerializer(serializers.ModelSerializer):
    """Сериализатор модели курсов (кратко)."""
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return get_avg_rating(ReviewCourse, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'rating', 'reviews',
                  'description', 'album', 'price']


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор модели курсов."""
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    album = AlbumSerializer(many=True)
    area = AreaSerializer()
    underground = UndergroundSerializer(many=True)

    def get_rating(self, obj):
        return get_avg_rating(ReviewCourse, obj)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'rating', 'reviews',
                  'album', 'description', 'telephone',
                  'address', 'price', 'email',
                  'underground', 'area', 'age']
