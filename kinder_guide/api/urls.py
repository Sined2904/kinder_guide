from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SchoolViewSet, KindergartensViewSet, CourseViewSet


app_name = 'api'

router = DefaultRouter()

router.register('schools', SchoolViewSet, basename='schools')
router.register('kindergartens', KindergartensViewSet, basename='kindergartens')
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
]