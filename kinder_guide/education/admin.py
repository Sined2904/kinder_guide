from django.contrib import admin

from .models import (AgeCategory, Area, Class, Favourites_Kindergartens,
                     Favourites_School, GroupSize, KindergartenAlbum,
                     Kindergartens, Language, Profile, School, SchoolAlbum,
                     Underground, WorkingHours, SchoolAverageRating,
                     KindergartenAverageRating)


class UndergroundAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class AgeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


# Школа
class SchoolAlbumInline(admin.TabularInline):
    model = SchoolAlbum


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'telephone',
                    'address', 'price', 'price_of_year', 'email',
                    'area', 'working_hours', 'website')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name', ]
    inlines = [SchoolAlbumInline, ]


class Favourites_SchoolAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user', ]


# Детский сад
class GroupSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class KindergartenAlbumInline(admin.TabularInline):
    model = KindergartenAlbum


class KindergartensAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',
                    'telephone', 'address', 'price',
                    'email', 'area', 'website',
                    'price_of_year')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name', ]
    inlines = [KindergartenAlbumInline, ]


class Favourites_KindergartensAdmin(admin.ModelAdmin):
    list_display = ('user', 'kindergartens')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user', ]


class SchoolAverageRatingAdmin(admin.ModelAdmin):
    list_display = ('school', 'average_rating')
    empty_value_display = '-пусто-'
    search_fields = ('school', )
    ordering = ['school', ]


class KindergartenAverageRatingAdmin(admin.ModelAdmin):
    list_display = ('kindergarten', 'average_rating')
    empty_value_display = '-пусто-'
    search_fields = ('Kindergarten', )
    ordering = ['kindergarten', ]


admin.site.register(GroupSize, GroupSizeAdmin)
admin.site.register(WorkingHours, WorkingHoursAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Underground, UndergroundAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AgeCategory, AgeCategoryAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Kindergartens, KindergartensAdmin)
admin.site.register(Favourites_School, Favourites_SchoolAdmin)
admin.site.register(Favourites_Kindergartens, Favourites_KindergartensAdmin)
admin.site.register(SchoolAverageRating, SchoolAverageRatingAdmin)
admin.site.register(KindergartenAverageRating, KindergartenAverageRatingAdmin)
