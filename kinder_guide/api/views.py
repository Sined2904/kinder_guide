from rest_framework import viewsets, status
from education.models import School, Favourites_School
from .serializers import SchoolSerializer, SchoolShortSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action


class SchoolViewSet(viewsets.ModelViewSet):
    '''Вьюсет для Тегов.'''

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_object(self):
        return get_object_or_404(School, id=self.kwargs['id'])

    def list(self, request):
        queryset = School.objects.all()
        paginate_queryset = self.paginate_queryset(queryset)
        serializer = SchoolShortSerializer(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = School.objects.all()
        school = get_object_or_404(queryset, pk=pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    @action(methods=['post', 'delete'], detail=True)
    def favorite(self, request, pk):
        school = get_object_or_404(School, id=pk)
        school_in_favorite = Favourites_school.objects.filter(
                user=request.user,
                school=school
            )
        if request.method == 'DELETE':
            if school_in_favorite.exists():
                school_in_favorite.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {'errors': 'Вы уже отписались или не были подписаны'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            if school_in_favorite.exists():
                return Response({'errors': 'Вы уже подписались'})
            Favourites_school.objects.create(user=request.user, school=school)
            return Response(status=status.HTTP_201_CREATED)