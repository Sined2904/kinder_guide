from rest_framework import viewsets, status
from education.models import School, Favourites_School, Kindergartens, Favourites_Kindergartens, Course, Favourites_Course
from .serializers import SchoolSerializer, SchoolShortSerializer, KindergartensShortSerializer, CourseShortSerializer, KindergartensSerializer, CourseSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action


class SchoolViewSet(viewsets.ModelViewSet):
    '''Вьюсет для Школы.'''

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_object(self):
        return get_object_or_404(School, id=self.kwargs['id'])

    def list(self, request):
        queryset = School.objects.all()
        paginate_queryset = self.paginate_queryset(queryset)
        serializer = SchoolShortSerializer(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = School.objects.all()
        school = get_object_or_404(queryset, pk=pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    @action(methods=['post', 'delete'], detail=True)
    def favorite(self, request, pk):
        school = get_object_or_404(School, id=pk)
        school_in_favorite = Favourites_School.objects.filter(
                user=request.user,
                school=school
            )
        if request.method == 'DELETE':
            if school_in_favorite.exists():
                school_in_favorite.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {'errors': 'Вы уже отписались или не были подписаны'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            if school_in_favorite.exists():
                return Response({'errors': 'Вы уже подписались'})
            Favourites_School.objects.create(user=request.user, school=school)
            return Response(status=status.HTTP_201_CREATED)
        

class KindergartensViewSet(viewsets.ModelViewSet):
    '''Вьюсет для Десткого сада.'''

    queryset = Kindergartens.objects.all()
    serializer_class = KindergartensSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_object(self):
        return get_object_or_404(Kindergartens, id=self.kwargs['id'])

    def list(self, request):
        queryset = Kindergartens.objects.all()
        paginate_queryset = self.paginate_queryset(queryset)
        serializer = KindergartensShortSerializer(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Kindergartens.objects.all()
        kindergarten = get_object_or_404(queryset, pk=pk)
        serializer = KindergartensSerializer(kindergarten)
        return Response(serializer.data)

    @action(methods=['post', 'delete'], detail=True)
    def favorite(self, request, pk):
        kindergarten = get_object_or_404(Kindergartens, id=pk)
        kindergarten_in_favorite = Favourites_Kindergartens.objects.filter(
                user=request.user,
                kindergarten=kindergarten
            )
        if request.method == 'DELETE':
            if kindergarten_in_favorite.exists():
                kindergarten_in_favorite.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {'errors': 'Вы уже отписались или не были подписаны'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            if kindergarten_in_favorite.exists():
                return Response({'errors': 'Вы уже подписались'})
            Favourites_Kindergartens.objects.create(user=request.user, kindergartens=kindergarten)
            return Response(status=status.HTTP_201_CREATED)
        

class CourseViewSet(viewsets.ModelViewSet):
    '''Вьюсет для Курсов.'''

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_object(self):
        return get_object_or_404(Course, id=self.kwargs['id'])

    def list(self, request):
        queryset = Course.objects.all()
        paginate_queryset = self.paginate_queryset(queryset)
        serializer = CourseShortSerializer(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Kindergartens.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    @action(methods=['post', 'delete'], detail=True)
    def favorite(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        course_in_favorite = Favourites_Course.objects.filter(
                user=request.user,
                course=course
            )
        if request.method == 'DELETE':
            if course_in_favorite.exists():
                course_in_favorite.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {'errors': 'Вы уже отписались или не были подписаны'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            if course_in_favorite.exists():
                return Response({'errors': 'Вы уже подписались'})
            Favourites_Course.objects.create(user=request.user, course=course)
            return Response(status=status.HTTP_201_CREATED)