from requests import Response
from rest_framework import status, viewsets

from .constants import UNAUTHORIZED
from .models import ReviewCourse, ReviewKindergarten, ReviewSchool
from .serializers import (ReviewCourseSerializer, ReviewKindergartenSerializer,
                          ReviewSchoolSerializer)


class ReviewSchoolViewSet(viewsets.ModelViewSet):
    queryset = ReviewSchool.objects.all()
    serializer_class = ReviewSchoolSerializer

    def get_queryset(self, request, *args, **kwargs):
        school_id = self.kwargs.get('school_id')
        return ReviewSchool.objects.filter(review_post=school_id).order_by('-id')

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            serializer.save(user=request.user, school_id=self.kwargs['school_id'])
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        else:
            return Response(UNAUTHORIZED, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
