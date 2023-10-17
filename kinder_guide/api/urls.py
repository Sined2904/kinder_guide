from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from .views import SchoolViewSet, KindergartensViewSet, CourseViewSet
from news.feeds import LatestNewsFeed

app_name = 'api'

router = DefaultRouter()

router.register('schools', SchoolViewSet, basename='schools')
router.register('kindergartens', KindergartensViewSet, basename='kindergartens')
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('feed/', LatestNewsFeed(), name = 'news_feed'),
]