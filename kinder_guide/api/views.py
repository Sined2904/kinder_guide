from comments.models import ReviewKindergarten, ReviewSchool
from django.shortcuts import get_object_or_404
from education.models import (Favourites_Kindergartens, Favourites_School,
                              Kindergartens, School)
from rest_framework import status, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdminOrReadOnly
from .serializers import (FilterKindergartenSerializer, FilterSchoolSerializer,
                          KindergartensSerializer,
                          KindergartensShortSerializer,
                          ReviewKindergartenSerializer, ReviewSchoolSerializer,
                          SchoolSerializer, SchoolShortSerializer)


class ReviewKindergartenViewSet(viewsets.ModelViewSet):
    """Вьюсет для Отзывов Десткого сада."""

    queryset = ReviewKindergarten.objects.all()
    serializer_class = ReviewKindergartenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, kindergarten_id):
        kindergarten_id = self.kwargs.get('kindergarten_id')
        queryset = self.queryset.filter(review_post_id=kindergarten_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, kindergarten_id):
        request.data['author'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(review_post_id=kindergarten_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, kindergarten_id, review_id):
        try:
            review = ReviewKindergarten.objects.get(
                id=review_id,
                review_post_id=kindergarten_id
            )
        except ReviewKindergarten.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewSchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для Отзывов школ."""

    queryset = ReviewSchool.objects.all()
    serializer_class = ReviewSchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, school_id):
        school_id = self.kwargs.get('school_id')
        queryset = self.queryset.filter(review_post_id=school_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, school_id):
        request.data['author'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(review_post_id=school_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, school_id, review_id):
        try:
            review = ReviewSchool.objects.get(
                id=review_id,
                review_post_id=school_id
            )
        except ReviewSchool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для Школы."""

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        """Переопределение сериализатора для POST запроса."""
        if list():
            return SchoolShortSerializer
        return SchoolSerializer

    # @action(methods=['post', 'delete'], detail=True)
    # def favorite(self, request, pk):
    #     """Добавляет школу в избранное"""

    #     school = get_object_or_404(School, id=pk)
    #     school_in_favorite = Favourites_School.objects.filter(
    #         user=request.user,
    #         school=school
    #     )
    #     if request.method == 'DELETE':
    #         if school_in_favorite.exists():
    #             school_in_favorite.delete()
    #             return Response(status=status.HTTP_204_NO_CONTENT)
    #         return Response(
    #             {'errors': 'Вы уже отписались или не были подписаны'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     else:
    #         if school_in_favorite.exists():
    #             return Response({'errors': 'Вы уже подписались'})
    #         Favourites_School.objects.create(user=request.user, school=school)
    #         return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST', 'DELETE'])
    def favorite(self, request, pk=None):
        """Добавляет школу в избранное"""
    
        user = request.user
        school = get_object_or_404(School, pk=pk)

        if request.method == 'POST':
            favorite, created = Favourites_School.objects.get_or_create(user=user, school=school)
            if created:
                school.is_favorited = True
                school.save()
                return Response({'detail': 'Школа успешно добавлена в избранное'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'Школа уже в избранном'}, status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            try:
                favorite = Favourites_School.objects.get(user=user, school=school)
            except Favourites_School.DoesNotExist:
                return Response({'detail': 'Школа не в избранном'}, status=status.HTTP_400_BAD_REQUEST)

            favorite.delete()
            school.is_favorited = False
            school.save()
            return Response({'detail': 'Школа успешно удалена из избранного'}, status=status.HTTP_204_NO_CONTENT)


class FilterSchoolView(APIView):
    """Вьюсет фильтров модели школы."""

    def get(self, request):
        schools = School.objects.all()
        serializer = FilterSchoolSerializer(schools, many=True)
        return Response(serializer.data)


class KindergartensViewSet(viewsets.ModelViewSet):
    """Вьюсет для Десткого сада."""

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

    @action(detail=True, methods=['POST', 'DELETE'])
    def favorite(self, request, pk=None):
        user = request.user
        school = get_object_or_404(School, pk=pk)

        if request.method == 'POST':
            # Добавить школу в избранное и установить is_favorited в True
            Favourites_School.create(user=user, school=school)
            school.is_favorited = True
            school.save()
            return Response({'detail': 'Школа успешно добавлена в избранное'}, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            try:
                favorite = Favourites_School.objects.get(user=user, school=school)
            except Favourites_School.DoesNotExist:
                return Response({'detail': 'Школа не найдена в избранном'}, status=status.HTTP_400_BAD_REQUEST)

            favorite.delete()
            school.is_favorited = False
            school.save()
            return Response({'detail': 'Школа успешно удалена из избранного'}, status=status.HTTP_204_NO_CONTENT)


class FilterKindergartenView(APIView):
    """Вьюсет фильтров модели детского сада."""

    def get(self, request):
        kindergartens = Kindergartens.objects.all()
        serializer = FilterKindergartenSerializer(kindergartens, many=True)
        return Response(serializer.data)