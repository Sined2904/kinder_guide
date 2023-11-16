from api.utils import get_avg_rating
from comments.models import ReviewKindergarten, ReviewSchool
from django.db import transaction
from django.db.models import Count, F
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from education.models import (AgeCategory, Area, Class,
                              Favourites_Kindergartens, Favourites_School,
                              GroupSize, KindergartenAverageRating,
                              Kindergartens, Language, Profile, School,
                              SchoolAverageRating, Underground, WorkingHours)
from news.models import News
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .filters import KindergartenFilter, SchoolFilter
from .permissions import IsAdminOrReadOnly
from .serializers import (AgeCategorySerializer, AreaSerializer,
                          ClassSerializer, GroupSizeSerializer,
                          KindergartensAddToFavouritesSerializer,
                          KindergartensSerializer,
                          KindergartensShortSerializer, LanguageSerializer,
                          NewsSerializer, ProfileSerializer,
                          ReviewKindergartenSerializer, ReviewSchoolSerializer,
                          SchoolAddToFavouritesSerializer, SchoolSerializer,
                          SchoolShortSerializer, UndergroundSerializer,
                          WorkingHoursSerializer)


class ReviewKindergartenViewSet(viewsets.ModelViewSet):
    """Вьюсет для отзывов десткого сада."""

    queryset = ReviewKindergarten.objects.all()
    serializer_class = ReviewKindergartenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, kindergarten_id):
        try:
            _ = Kindergartens.objects.get(id=kindergarten_id)
        except Kindergartens.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        kindergarten_id = self.kwargs.get('kindergarten_id')
        queryset = self.queryset.filter(review_post_id=kindergarten_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, kindergarten_id, review_id):
        try:
            review = ReviewKindergarten.objects.get(
                id=review_id,
                review_post_id=kindergarten_id
            )
        except ReviewKindergarten.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(review)
        return Response(serializer.data)

    def create(self, request, kindergarten_id):
        try:
            _ = Kindergartens.objects.get(id=kindergarten_id)
        except Kindergartens.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data['author'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(review_post_id=kindergarten_id)
        update_kindergarten_avg_rating(kindergarten_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, kindergarten_id, review_id):
        try:
            review = ReviewKindergarten.objects.get(
                id=review_id,
                review_post_id=kindergarten_id
            )
        except ReviewKindergarten.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if review.author != request.user:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data='У вас нет разрешения удалять этот отзыв'
            )
        review.delete()
        update_kindergarten_avg_rating(kindergarten_id)
        return Response(status=status.HTTP_204_NO_CONTENT, data='Удалено')

    def patch(self, request, kindergarten_id, review_id):
        try:
            review = get_object_or_404(
                ReviewKindergarten, id=review_id,
                review_post_id=kindergarten_id
            )
            self.check_object_permissions(request, review)
        except ReviewKindergarten.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if review.author != request.user:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data="У вас нет разрешения редактировать этот отзыв"
            )
        serializer = self.get_serializer(
            review, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        update_kindergarten_avg_rating(kindergarten_id)

        return Response(serializer.data)


class ReviewSchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для отзывов школ."""

    queryset = ReviewSchool.objects.all()
    serializer_class = ReviewSchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, school_id):
        try:
            _ = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        school_id = self.kwargs.get('school_id')
        queryset = self.queryset.filter(review_post_id=school_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, school_id, review_id):
        try:
            review = ReviewSchool.objects.get(
                id=review_id,
                review_post_id=school_id
            )
        except ReviewSchool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(review)
        return Response(serializer.data)

    def create(self, request, school_id):
        try:
            _ = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data['author'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(review_post_id=school_id)
        update_school_avg_rating(school_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, school_id, review_id):
        try:
            review = ReviewSchool.objects.get(
                id=review_id,
                review_post_id=school_id
            )
        except ReviewSchool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if review.author != request.user:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data='У вас нет разрешения удалять этот отзыв'
            )
        review.delete()
        update_school_avg_rating(school_id)

        return Response(status=status.HTTP_204_NO_CONTENT, data='Удалено')

    def patch(self, request, school_id, review_id):
        try:
            review = get_object_or_404(
                ReviewSchool, id=review_id,
                review_post_id=school_id
            )
            self.check_object_permissions(request, review)
        except ReviewSchool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if review.author != request.user:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data="У вас нет разрешения редактировать этот отзыв"
            )
        serializer = self.get_serializer(
            review, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        update_school_avg_rating(school_id)

        return Response(serializer.data)


class SchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для школы."""

    queryset = School.objects.annotate(reviews_count=Count("reviews"))
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    filterset_class = SchoolFilter
    ordering_fields = (
        'name',
        'price',
        'rating',
        'reviews_count',
    )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    search_fields = ('name', 'description',
                     'telephone', 'address',
                     'email', 'website'
                     )

    def get_queryset(self):
        query = super().get_queryset().annotate(
            rating=F('schoolaveragerating__average_rating')
        )
        return query

    def filter_queryset(self, queryset):
        value = self.request.query_params.get('ordering')
        qs = queryset
        if value and any(v in ['reviews', '-reviews'] for v in value):
            qs = qs.annotate(reviews_count=Count("schoolreviews"))
            if 'reviews' in value:
                qs = qs.order_by("reviews")
            elif '-reviews' in value:
                qs = qs.order_by("-reviews")

        return super().filter_queryset(qs)

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
            return Response(
                {'detail': 'Школа успешно удалена из избранного'},
                status=status.HTTP_204_NO_CONTENT
            )

    @action(detail=False, methods=['get'])
    def all(self, request):
        """Выводит все объекты без пагинации."""
        schools = School.objects.all()
        serializer = SchoolSerializer(
            schools,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class KindergartensViewSet(viewsets.ModelViewSet):
    """Вьюсет для десткого сада."""

    queryset = Kindergartens.objects.annotate(reviews_count=Count("reviews"))
    serializer_class = KindergartensSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_class = KindergartenFilter
    ordering_fields = (
        'name',
        'price',
        'rating',
        'reviews_count',
    )
    search_fields = ('name', 'description',
                     'telephone', 'address',
                     'email', 'website')

    def get_queryset(self):
        query = super().get_queryset().annotate(
            rating=F('kindergartenaveragerating__average_rating')
        )
        return query

    def filter_queryset(self, queryset):
        value = self.request.query_params.get('ordering')
        qs = queryset
        if value and any(v in ['reviews', '-reviews'] for v in value):
            qs = qs.annotate(reviews_count=Count("kindergartenreviews"))
            if 'reviews' in value:
                qs = qs.order_by("reviews")
            elif '-reviews' in value:
                qs = qs.order_by("-reviews")

        return super().filter_queryset(qs)

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
        kindergartens = get_object_or_404(Kindergartens, pk=pk)
        if request.method == 'POST':
            favorite, created = Favourites_Kindergartens.objects.get_or_create(
                user=user,
                kindergartens=kindergartens
            )
            if created:
                kindergartens.is_favorited = True
                kindergartens.save()
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
                    kindergartens=kindergartens
                )
            except Favourites_Kindergartens.DoesNotExist:
                return Response(
                    {'detail': 'Детский сад не в избранном'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            favorite.delete()
            return Response(
                {'detail': 'Детский сад успешно удален из избранного'},
                status=status.HTTP_204_NO_CONTENT
            )

    @action(detail=False, methods=['get'])
    def all(self, request):
        """Выводит все объекты без пагинации."""
        kindergartens = Kindergartens.objects.all()
        serializer = KindergartensSerializer(
            kindergartens,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class UndergroundViewSet(viewsets.ModelViewSet):
    """Вьюсет для метро."""

    queryset = Underground.objects.all()
    serializer_class = UndergroundSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class AreaViewSet(viewsets.ModelViewSet):
    """Вьюсет для округа."""

    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class LanguageViewSet(viewsets.ModelViewSet):
    """Вьюсет для языков."""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class ProfileViewSet(viewsets.ModelViewSet):
    """Вьюсет для профилей."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class WorkingHoursViewSet(viewsets.ModelViewSet):
    """Вьюсет для часов работы."""

    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class ClassViewSet(viewsets.ModelViewSet):
    """Вьюсет для классов."""

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class AgeCategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для возрастных категорий."""

    queryset = AgeCategory.objects.all()
    serializer_class = AgeCategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class GroupSizeViewSet(viewsets.ModelViewSet):
    """Вьюсет для размера группы."""

    queryset = GroupSize.objects.all()
    serializer_class = GroupSizeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class FavoriteSchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для избранного школы."""

    queryset = School.objects.all()
    serializer_class = SchoolShortSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    def get_queryset(self):
        schools = School.objects.filter(
            favourites_users__user=self.request.user
        )
        return schools

    def list(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response('Для получения избранного, авторизируйтесь')
        return super().list(request, *args, **kwargs)


class FavoriteKindergartenViewSet(viewsets.ModelViewSet):
    """Вьюсет для избранного сады."""

    queryset = Kindergartens.objects.all()
    serializer_class = KindergartensShortSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    def get_queryset(self):
        kindergartes = Kindergartens.objects.filter(
            favourites_users__user=self.request.user
        )
        return kindergartes

    def list(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response('Для получения избранного, авторизируйтесь')
        return super().list(request, *args, **kwargs)


class NewsViewSet(viewsets.ModelViewSet):
    """Вьюсет для новостей."""

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class AddFavoriteSchoolViewSet(viewsets.ViewSet):
    """Вьюсет для добавления избранного школы после регистрации."""

    queryset = School.objects.all()
    serializer_class = SchoolAddToFavouritesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        id_schools = request.data['school']
        for i in id_schools:
            Favourites_School.objects.create(
                user=request.user,
                school=get_object_or_404(School, id=i)
            )
        return Response('Все школы добавлены в избранное',
                        status=status.HTTP_201_CREATED)


class AddFavoriteKindergartenViewSet(viewsets.ModelViewSet):
    """Вьюсет для добавления избранного сады после регистрации."""

    queryset = Kindergartens.objects.all()
    serializer_class = KindergartensAddToFavouritesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        id_kindergartens = request.data['kindergartens']
        for i in id_kindergartens:
            Favourites_Kindergartens.objects.create(
                user=request.user,
                kindergartens=get_object_or_404(Kindergartens, id=i)
            )
        return Response('Все сады добавлены в избранное',
                        status=status.HTTP_201_CREATED)


def update_school_avg_rating(school_id):
    school = get_object_or_404(School, id=school_id)
    avg_rating = get_avg_rating(ReviewSchool, school)
    school_avg_rating, _ = SchoolAverageRating.objects.get_or_create(
        school=school
    )
    school_avg_rating.average_rating = avg_rating
    school_avg_rating.save()


def update_kindergarten_avg_rating(kindergarten_id):
    kindergarten = get_object_or_404(Kindergartens, id=kindergarten_id)
    avg_rating = get_avg_rating(ReviewKindergarten, kindergarten)
    kindergarten_avg_rating, _ = (
        KindergartenAverageRating.objects.get_or_create(
            kindergarten=kindergarten
        )
    )
    kindergarten_avg_rating.average_rating = avg_rating
    kindergarten_avg_rating.save()
