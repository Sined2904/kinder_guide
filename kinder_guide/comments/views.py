from requests import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ReviewCourse, ReviewKindergarten, ReviewSchool
from .serializers import (ReviewCourseSerializer, ReviewKindergartenSerializer,
                          ReviewSchoolSerializer)


class ReviewCoursesViewSet(viewsets.ModelViewSet):
    queryset = ReviewCourse.objects.all()
    serializer_class = ReviewCourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ReviewKindergartenViewSet(viewsets.ModelViewSet):
    queryset = ReviewKindergarten.objects.all()
    serializer_class = ReviewKindergartenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ReviewSchoolViewSet(viewsets.ModelViewSet):
    queryset = ReviewSchool.objects.all()
    serializer_class = ReviewSchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
