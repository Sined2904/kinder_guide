from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SchoolViewSet


app_name = 'api'

router = DefaultRouter()

router.register('schools', SchoolViewSet, basename='schools')


urlpatterns = [
    path('', include(router.urls)),
]