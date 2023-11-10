from django.urls import include, path
from djoser import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as token_views

from .views import (AgeCategoryViewSet, AreaViewSet, ClassViewSet,
                    FavoriteKindergartenViewSet, FavoriteSchoolViewSet,
                    GroupSizeViewSet, KindergartensViewSet, LanguageViewSet,
                    NewsViewSet, ProfileViewSet, ReviewKindergartenViewSet,
                    ReviewSchoolViewSet, SchoolViewSet, UndergroundViewSet,
                    WorkingHoursViewSet, AddFavoriteKindergartenViewSet,
                    AddFavoriteSchoolViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('schools', SchoolViewSet, basename='schools')
router.register('kindergartens',
                KindergartensViewSet,
                basename='kindergartens'
                )
router.register('underground', UndergroundViewSet, basename='underground')
router.register('area', AreaViewSet, basename='area')
router.register('language', LanguageViewSet, basename='language')
router.register('profile', ProfileViewSet, basename='profile')
router.register('agecategory', AgeCategoryViewSet, basename='agecategory')
router.register('groupsize', GroupSizeViewSet, basename='groupsize')
router.register('class', ClassViewSet, basename='class')
router.register('workinghours', WorkingHoursViewSet, basename='workinghours')
router.register('news', NewsViewSet, basename='news')


urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/auth/signup/',
        views.UserViewSet.as_view({'post': 'create'}),
        name='signup',
    ),
    path(
        'v1/auth/signin/',
        token_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'v1/auth/reset/',
        views.UserViewSet.as_view({'post': 'reset_password'}),
        name='reset_password',
    ),
    path(
        'v1/auth/reset/confirm/',
        views.UserViewSet.as_view({'post': 'reset_password_confirm'}),
        name='reset_password',
    ),
    path(
        "v1/me/",
        views.UserViewSet.as_view({"get": "me",
                                   "put": "me",
                                   "patch": "me",
                                   "delete": "me"}),
        name="me",
    ),
    path(
        "v1/me/favoritekindergartens/",
        FavoriteKindergartenViewSet.as_view({'get': 'list'}),
        name="favoritekindergartens",
    ),
    path(
        "v1/me/favoriteschools/",
        FavoriteSchoolViewSet.as_view({'get': 'list'}),
        name="favoriteschools",
    ),
    path(
        "v1/me/add_favoritekindegartens/",
        AddFavoriteKindergartenViewSet.as_view({'post': 'create'}),
        name="favoritekindergartens",
    ),
    path(
        "v1/me/add_favoriteschools/",
        AddFavoriteSchoolViewSet.as_view({'post': 'create'}),
        name="favoriteschools",
    ),
    path(
        'v1/kindergartens/<int:kindergarten_id>/reviews/',
        ReviewKindergartenViewSet.as_view(
            {'get': 'list', 'post': 'create'}
        ),
        name='kindergartens_reviews',
    ),
    path(
        'v1/kindergartens/<int:kindergarten_id>/reviews/<int:review_id>/',
        ReviewKindergartenViewSet.as_view(
            {'delete': 'delete', 'patch': 'patch'}
        ),
        name='schools_review_update',
    ),
    path(
        'v1/schools/<int:school_id>/reviews/',
        ReviewSchoolViewSet.as_view(
            {'get': 'list', 'post': 'create'}
        ),
        name='schools_reviews',
    ),
    path(
        'v1/schools/<int:school_id>/reviews/<int:review_id>/',
        ReviewSchoolViewSet.as_view(
            {'delete': 'delete', 'patch': 'patch'}
        ),
        name='schools_review_update',
    ),
]
