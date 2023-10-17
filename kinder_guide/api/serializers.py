from django.shortcuts import get_object_or_404
from rest_framework import serializers
from education.models import School, Kindergartens, Course


class SchoolShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'album', 'price']


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['name', 'album', 'description',
                    'telephone', 'address', 'price', 'price_of_year', 
                    'email', 'classes', 'name_author', 'underground', 
                    'area', 'languages', 'profile', 'age']


class KindergartensShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kindergartens
        fields = ['id', 'name', 'description', 'album', 'price']


class KindergartensSerializer(serializers.ModelSerializer):

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

    class Meta:
        model = Course
        fields = ['id', 'name', 'album', 'description',
                    'telephone', 'address', 'price', 
                    'email', 'underground', 
                    'area', 'age']