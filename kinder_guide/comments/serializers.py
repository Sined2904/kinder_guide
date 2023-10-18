from rest_framework import serializers

from .models import ReviewCourse, ReviewKindergarten, ReviewSchool


class ReviewSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField(source='rating')


class ReviewSchoolSerializer(ReviewSerializer):
    class Meta:
        model = ReviewSchool
        fields = ['id', 'content', 'grade', 'author', 'date_posted']


class ReviewCourseSerializer(ReviewSerializer):
    class Meta:
        model = ReviewCourse
        fields = ['id', 'content', 'grade', 'author', 'date_posted']


class ReviewKindergartenSerializer(ReviewSerializer):
    class Meta:
        model = ReviewKindergarten
        fields = ['id', 'content', 'grade', 'author', 'date_posted']
