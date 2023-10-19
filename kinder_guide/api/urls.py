from django.urls import include, path
from djoser import views
from news.feeds import LatestNewsFeed
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as token_views

from .views import (CourseViewSet, KindergartensViewSet, ReviewCoursesViewSet,
                    ReviewKindergartenViewSet, ReviewSchoolViewSet,
                    SchoolViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('schools', SchoolViewSet, basename='schools')
router.register('kindergartens', KindergartensViewSet, basename='kindergartens')
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        "auth/signup",
        views.UserViewSet.as_view({"post": "create"}),
        name="signup",
    ),
    path(
        "auth/signin",
        token_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "auth/reset",
        views.UserViewSet.as_view({"post": "reset_password"}),
        name="reset_password",
    ),
    path(
        "auth/reset/confirm/",
        views.UserViewSet.as_view({"post": "reset_password_confirm"}),
        name="reset_password",
    ),
    path(
        "me/",
        views.UserViewSet.as_view({"get": "me", "put": "me", "patch": "me", "delete": "me"}),
        name="me",
    ),
    path(
        'courses/<int:courses_id>/reviews/',
        ReviewCoursesViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'delete', 'update': 'update'}),
        name='courses_reviews'
    ),
    path(
        'kindergartens/<int:kindergarten_id>/reviews/',
        ReviewKindergartenViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'delete', 'update': 'update'}),
        name='kindergartens_reviews',
    ),
    path(
        'schools/<int:school_id>/reviews/',
        ReviewSchoolViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'delete', 'update': 'update'}),
        name='schools_reviews',
    ),
    # path('auth/', include('djoser.urls')),
    path('feed/', LatestNewsFeed(), name = 'news_feed'),
]
