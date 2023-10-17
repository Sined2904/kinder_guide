from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SchoolViewSet, KindergartensViewSet, CourseViewSet
from news.feeds import LatestNewsFeed
from djoser import views
from rest_framework_simplejwt import views as token_views

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
    path('auth/', include('djoser.urls')),
    path('feed/', LatestNewsFeed(), name = 'news_feed'),
]