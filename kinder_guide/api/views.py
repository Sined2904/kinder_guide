from django_filters.rest_framework import DjangoFilterBackend

from education.models import Language, Profile, Education


class EducationViewSet(viewsets.ModelViewSet):
    """Эндпоинт для работы с моделью Education"""
    queryset = Education.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = 


    def perform_update(self, serializer):
        super(EducationViewSet, self).perform_update(serializer)