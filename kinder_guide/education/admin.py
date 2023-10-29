from django.contrib import admin

from .models import (Language, Profile, School, Favourites_School,
                     Sport, Create, Intelligence, Music, Kindergartens,
                     Favourites_Kindergartens, Course, Favourites_Course,
                     Underground, CourseAlbum, SchoolAlbum)


class UndergroundAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


# Школа
class SchoolAlbumInline(admin.TabularInline):
    model = SchoolAlbum


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'telephone',
                    'address', 'price', 'price_of_year', 'email',
                    'classes', 'name_author', 'area', 'age', 'working_hours')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]
    inlines = [SchoolAlbumInline]

class Favourites_SchoolAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user',]


# Детский сад
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


class CreateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


class IntelligenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


class KindergartensAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'telephone', 'address', 'price',
                    'email', 'area', 'age', 'price_of_year', 'working_hours',
                    'group_suze')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]


class Favourites_KindergartensAdmin(admin.ModelAdmin):
    list_display = ('user', 'kindergartens')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user',]


# Курсы
class CourseAlbumInline(admin.TabularInline):
    model = CourseAlbum


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',
                    'telephone', 'address', 'price',
                    'email', 'underground',
                    'area', 'age')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]
    inlines = [CourseAlbumInline]


class Favourites_CourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user',]


admin.site.register(Underground, UndergroundAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Create, CreateAdmin)
admin.site.register(Intelligence, IntelligenceAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Kindergartens, KindergartensAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Favourites_School, Favourites_SchoolAdmin)
admin.site.register(Favourites_Kindergartens, Favourites_KindergartensAdmin)
admin.site.register(Favourites_Course, Favourites_CourseAdmin)
