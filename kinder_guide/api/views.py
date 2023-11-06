from comments.models import ReviewKindergarten, ReviewSchool
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from education.models import (Favourites_Kindergartens, Favourites_School,
                              Kindergartens, School, Underground, Area,
                              Language, Profile, AgeCategory, Sport, Create,
                              Intelligence, Music)
from news.models import News
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly
from .serializers import (KindergartensSerializer,
                          KindergartensShortSerializer,
                          ReviewKindergartenSerializer, ReviewSchoolSerializer,
                          NewsSerializer, SchoolSerializer, SchoolShortSerializer,
                          UndergroundSerializer, LanguageSerializer,
                          AreaSerializer, SportSerializer, CreateSerializer,
                          MusicSerializer, IntelligenceSerializer,
                          ProfileSerializer, AgeCategorySerializer)


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'name', 'price', 'price_of_year')
    search_fields = ('name', 'description',
                     'telephone', 'address',
                     'email', 'website'
                     )

    def get_serializer_class(self):
        """Переопределение сериализатора для POST запроса."""
        if bool(self.kwargs) is False:
            return KindergartensShortSerializer
        return KindergartensSerializer

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


class UndergroundViewSet(viewsets.ModelViewSet):
    """Вьюсет для метро."""

    queryset = Underground.objects.all()
    serializer_class = UndergroundSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class AreaViewSet(viewsets.ModelViewSet):
    """Вьюсет для Округа."""

    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class LanguageViewSet(viewsets.ModelViewSet):
    """Вьюсет для Языков."""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class ProfileViewSet(viewsets.ModelViewSet):
    """Вьюсет для Профилей."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class AgeCategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для Возрастных категорий."""

    queryset = AgeCategory.objects.all()
    serializer_class = AgeCategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class SportViewSet(viewsets.ModelViewSet):
    """Вьюсет для Спортивных занятий."""

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class CreateViewSet(viewsets.ModelViewSet):
    """Вьюсет для Творческих занятий."""

    queryset = Create.objects.all()
    serializer_class = CreateSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class IntelligenceViewSet(viewsets.ModelViewSet):
    """Вьюсет для Интеллектуальных занятий."""

    queryset = Intelligence.objects.all()
    serializer_class = IntelligenceSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class MusicViewSet(viewsets.ModelViewSet):
    """Вьюсет для Музыкльных занятий."""

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class FavoriteSchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для избранного Школы."""

    queryset = School.objects.all()
    serializer_class = SchoolShortSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['GET'])
    def favoriteschool(self):
        schools = self.request.user.favourites_school
        serializer = SchoolShortSerializer(schools, many=True)
        return Response(serializer.data)


class FavoriteKindergartenViewSet(viewsets.ModelViewSet):
    """Вьюсет для избранного Сады."""

    queryset = Kindergartens.objects.all()
    serializer_class = KindergartensShortSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['GET'])
    def favoritekindergartens(self, request):
        kindergartes = self.request.user.favourites_kindergartens
        serializer = KindergartensShortSerializer(kindergartes, many=True)
        return Response(serializer.data)


class NewsViewSet(viewsets.ModelViewSet):
    """Вьюсет для новостей."""

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
