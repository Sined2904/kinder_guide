from requests import Response
from rest_framework import status, viewsets

from .constants import UNAUTHORIZED
from .models import ReviewCourse, ReviewKindergarten, ReviewSchool
from .serializers import (ReviewCourseSerializer, ReviewKindergartenSerializer,
                          ReviewSchoolSerializer)


class ReviewSchoolViewSet(viewsets.ModelViewSet):
    pass