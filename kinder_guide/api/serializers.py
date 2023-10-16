from django.shortcuts import get_object_or_404
from rest_framework import serializers
from education.models import School


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

        