from django.shortcuts import get_object_or_404
from rest_framework import serializers
from education.models import School, Kindergartens, Course, Underground, Language, Profile, Album

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

    class Meta:
        model = Album
        fields = ['image',]

class SchoolSerializer(serializers.ModelSerializer):
    #underground = UndergroundSerializer(many=True)
    #languages = LanguageSerializer(many=True)
    #profile = ProfileSerializer(many=True)
    album = AlbumSerializer(many=True)
    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'telephone', 
                  'address', 'underground', 'area', 'email', 
                  'album', 'price', 'price_of_year', 'age', 
                  'classes', 'languages', 'profile', 'name_author']


class KindergartensShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'description', 'album', 'price']


class KindergartensSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True)

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'album', 'description',
                    'telephone', 'address', 'price', 'price_of_year', 
                    'email', 'classes', 'name_author', 'underground', 
                    'area', 'languages', 'profile', 'age', 'working_hours',
                    'group_suze', 'sport_dev', 'create_dev', 'music_dev', 'intel_dev']


class CourseShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'album', 'price']


class CourseSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'album', 'description',
                    'telephone', 'address', 'price', 
                    'email', 'underground', 
                    'area', 'age']