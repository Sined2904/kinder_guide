from django_filters import FilterSet, NumberFilter
from django_filters import rest_framework as filters
from education.models import (School, Kindergartens, Profile, Class, Language,
                              Area, Underground, WorkingHours, GroupSize,
                              Development, AgeCategory)


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
    min_price = NumberFilter(name="price", lookup_type='gte')
    max_price = NumberFilter(name="price", lookup_type='lte')

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
    development = filters.ModelMultipleChoiceFilter(
        field_name='development__slug',
        to_field_name='slug',
        queryset=Development.objects.all(),
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
    min_price = NumberFilter(name="price", lookup_type='gte')
    max_price = NumberFilter(name="price", lookup_type='lte')

    class Meta:
        model = Kindergartens
        fields = ['working_hours', 'group_suze', 'development',
                  'preparing_for_school', 'age_category', 'area',
                  'underground', 'languages', 'area', 'min_price',
                  'max_price']
