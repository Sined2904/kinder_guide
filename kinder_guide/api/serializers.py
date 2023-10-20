
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from comments.models import ReviewCourse, ReviewKindergarten, ReviewSchool
from education.models import (Album, Course, Kindergartens, Language, Profile,
                              School, Underground, CourseAlbum)
from rest_framework import serializers
from .utils import get_avg_rating


class ReviewSerializer(serializers.ModelSerializer):
    '''Сериализатор отзывов'''
    grade = serializers.IntegerField(source='rating')


class ReviewSchoolSerializer(ReviewSerializer):
    '''Сериализатор отзывов школы'''
    class Meta:
        model = ReviewSchool
        fields = ['id', 'content', 'grade', 'author', 'date_posted']


class ReviewCourseSerializer(ReviewSerializer):
    '''Сериализатор отзывов курса'''
    class Meta:
        model = ReviewCourse
        fields = ['id', 'content', 'grade', 'author', 'date_posted']


class ReviewKindergartenSerializer(ReviewSerializer):
    '''Сериализатор отзывов детского сада'''
    class Meta:
        model = ReviewKindergarten
        fields = ['id', 'content', 'grade', 'author', 'date_posted']

'''
class UndergroundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Underground
        fields = ['name', 'slug']


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['name', 'slug']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['name', 'slug']
'''

class SchoolShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'album', 'price']


class AlbumSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Album
        fields = ['image',]


class SchoolSerializer(serializers.ModelSerializer):
    #underground = UndergroundSerializer(many=True)
    #languages = LanguageSerializer(many=True)
    #profile = ProfileSerializer(many=True)
    album = AlbumSerializer(many=True)
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return get_avg_rating(ReviewSchool)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = School
        fields = ['id', 'name', 'rating', 'reviews', 'description', 'telephone',
                  'address', 'underground', 'area', 'email',
                  'album', 'price', 'price_of_year', 'age',
                  'classes', 'languages', 'profile', 'name_author']


class KindergartensShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'description', 'album', 'price']


class KindergartensSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    album = AlbumSerializer(many=True)
    
    def get_rating(self, obj):
        return get_avg_rating(ReviewKindergarten)

    def get_reviews(self, obj):
        return obj.reviews.count()

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'rating', 'reviews', 'album', 'description',
                    'telephone', 'address', 'price', 'price_of_year',
                    'email', 'underground',
                    'area', 'languages', 'age','working_hours',
                    'group_suze', 'sport_dev', 'create_dev', 'music_dev', 'intel_dev']

class CourseAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseAlbum
        fields = ['image',]


class CourseShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'album', 'price']


def get_avg_rating(course):
    reviews = ReviewCourse.objects.filter(review_post=course)
    avg_rating = reviews.aggregate(Avg('rating'))
    return avg_rating['rating__avg'] or 0


class CourseSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    album = CourseAlbumSerializer(many=True)
    
    def get_rating(self, obj):
        return get_avg_rating(obj)
    
    def get_reviews(self, obj):
        return obj.reviews.count()


    class Meta:
        model = Course
        fields = ['id', 'name', 'rating', 'reviews', 'album', 'description',
                    'telephone', 'address', 'price',
                    'email', 'underground',
                    'area', 'age']
