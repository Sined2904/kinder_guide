from comments.models import ReviewKindergarten, ReviewSchool
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from education.models import (Favourites_Kindergartens, Favourites_School,
                              Kindergartens, School)
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


from .permissions import IsAdminOrReadOnly
from .serializers import (KindergartensSerializer,
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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'name', 'price', 'price_of_year')
    search_fields = ('name', 'description',
                     'telephone', 'address',
                     'email', 'website'
                     )
    
    def get_object(self):
        return get_object_or_404(School, pk=self.kwargs['pk'])

    def get_serializer_class(self):
        """Переопределение сериализатора для POST запроса."""
        if bool(self.kwargs) is False:
            return SchoolShortSerializer
        return SchoolSerializer

    @transaction.atomic
    @action(detail=True, methods=['POST', 'DELETE'])
    def favorite(self, request, pk=None):
        """Добавляет школу в избранное."""
        user = request.user
        school = get_object_or_404(School, pk=pk)
        if request.method == 'POST':
            favorite, created = Favourites_School.objects.get_or_create(
                user=user,
                school=school
            )
            if created:
                school.is_favorited = True
                school.save()
                return Response(
                    {'detail': 'Школа успешно добавлена в избранное'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'detail': 'Школа уже в избранном'},
                    status=status.HTTP_200_OK
                )

        elif request.method == 'DELETE':
            try:
                favorite = Favourites_School.objects.get(
                    user=user,
                    school=school
                )
            except Favourites_School.DoesNotExist:
                return Response(
                    {'detail': 'Школа не в избранном'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            favorite.delete()
            school.is_favorited = False
            school.save()
            return Response(
                {'detail': 'Школа успешно удалена из избранного'},
                status=status.HTTP_204_NO_CONTENT
            )


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

    @transaction.atomic
    @action(detail=True, methods=['POST', 'DELETE'])
    def favorite(self, request, pk=None):
        """Добавляет детский сад в избранное."""
        user = request.user
        kindergarten = get_object_or_404(School, pk=pk)

        if request.method == 'POST':
            favorite, created = Favourites_Kindergartens.objects.get_or_create(
                user=user,
                kindergarten=kindergarten
            )
            if created:
                kindergarten.is_favorited = True
                kindergarten.save()
                return Response(
                    {'detail': 'Детский сад успешно добавлен в избранное'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'detail': 'Детский сад уже в избранном'},
                    status=status.HTTP_200_OK
                )

        elif request.method == 'DELETE':
            try:
                favorite = Favourites_Kindergartens.objects.get(
                    user=user,
                    sckindergartenhool=kindergarten
                )
            except Favourites_Kindergartens.DoesNotExist:
                return Response(
                    {'detail': 'Детский сад не в избранном'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            favorite.delete()
            kindergarten.is_favorited = False
            kindergarten.save()
            return Response(
                {'detail': 'Детский сад успешно удален из избранного'},
                status=status.HTTP_204_NO_CONTENT
            )
