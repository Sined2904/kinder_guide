from django_filters import FilterSet, NumberFilter
from django_filters import rest_framework as filters
from education.models import (AgeCategory, Area, Class, GroupSize,
                              Kindergartens, Language, Profile, School,
                              Underground, WorkingHours)


class SchoolFilter(FilterSet):
    """Фильтр для школ."""

    profile = filters.ModelMultipleChoiceFilter(
        field_name='profile__slug',
        to_field_name='slug',
        queryset=Profile.objects.all(),
    )
    classes = filters.ModelMultipleChoiceFilter(
        field_name='classes__slug',
        to_field_name='slug',
        queryset=Class.objects.all(),
    )
    languages = filters.ModelMultipleChoiceFilter(
        field_name='languages__slug',
        to_field_name='slug',
        queryset=Language.objects.all(),
    )
    area = filters.ModelMultipleChoiceFilter(
        field_name='area__slug',
        to_field_name='slug',
        queryset=Area.objects.all(),
    )
    underground = filters.ModelMultipleChoiceFilter(
        field_name='underground__slug',
        to_field_name='slug',
        queryset=Underground.objects.all(),
    )
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte',)

    class Meta:
        model = School
        fields = ['profile', 'classes', 'languages',
                  'area', 'underground', 'min_price',
                  'max_price',]


class KindergartenFilter(FilterSet):
    """Фильтр для детских садов."""

    working_hours = filters.ModelMultipleChoiceFilter(
        field_name='working_hours__slug',
        to_field_name='slug',
        queryset=WorkingHours.objects.all(),
    )
    group_size = filters.ModelMultipleChoiceFilter(
        field_name='group_size__slug',
        to_field_name='slug',
        queryset=GroupSize.objects.all(),
    )
    age_category = filters.ModelMultipleChoiceFilter(
        field_name='age_category__slug',
        to_field_name='slug',
        queryset=AgeCategory.objects.all(),
    )
    languages = filters.ModelMultipleChoiceFilter(
        field_name='languages__slug',
        to_field_name='slug',
        queryset=Language.objects.all(),
    )
    area = filters.ModelMultipleChoiceFilter(
        field_name='area__slug',
        to_field_name='slug',
        queryset=Area.objects.all(),
    )
    underground = filters.ModelMultipleChoiceFilter(
        field_name='underground__slug',
        to_field_name='slug',
        queryset=Underground.objects.all(),
    )
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte',)
    create_dev = filters.BooleanFilter(
        field_name='kindergartens__create_dev',
        method='get_create_dev'
    )
    intel_dev = filters.BooleanFilter(
        field_name='kindergartens__intel_dev',
        method='get_intel_dev'
    )
    music_dev = filters.BooleanFilter(
        field_name='kindergartens__music_dev',
        method='get_music_dev'
    )
    sport_dev = filters.BooleanFilter(
        field_name='kindergartens__sport_dev',
        method='get_sport_dev'
    )

    def get_create_dev(self, queryset, name, value):
        if value is True:
            queryset = Kindergartens.objects.exclude(create_dev=None)
            return queryset
        return queryset

    def get_intel_dev(self, queryset, name, value):
        if value is True:
            queryset = Kindergartens.objects.exclude(intel_dev=None)
            return queryset
        return queryset

    def get_music_dev(self, queryset, name, value):
        if value is True:
            queryset = Kindergartens.objects.exclude(music_dev=None)
            return queryset
        return queryset

    def get_sport_dev(self, queryset, name, value):
        if value is True:
            queryset = Kindergartens.objects.exclude(sport_dev=None)
            return queryset
        return queryset

    class Meta:
        model = Kindergartens
        fields = ['working_hours', 'group_size',
                  'preparing_for_school', 'age_category', 'area',
                  'underground', 'languages', 'area', 'min_price',
                  'max_price', 'create_dev', 'intel_dev', 'music_dev',
                  'sport_dev', ]
