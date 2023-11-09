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
                  'max_price']


class KindergartenFilter(FilterSet):
    """Фильтр для детских садов."""

    working_hours = filters.ModelMultipleChoiceFilter(
        field_name='working_hours__slug',
        to_field_name='slug',
        queryset=WorkingHours.objects.all(),
    )
    group_suze = filters.ModelMultipleChoiceFilter(
        field_name='group_suze__slug',
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

    class Meta:
        model = Kindergartens
        fields = ['working_hours', 'group_suze',
                  'preparing_for_school', 'age_category', 'area',
                  'underground', 'languages', 'area', 'min_price',
                  'max_price']
