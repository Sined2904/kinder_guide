from rest_framework import serializers

from .models import ReviewCourse, ReviewKindergarten, ReviewSchool


class ReviewSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSchool
        fields = '__all__'


class ReviewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCourse
        fields = '__all__'


class ReviewKindergartenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewKindergarten
        fields = '__all__'
