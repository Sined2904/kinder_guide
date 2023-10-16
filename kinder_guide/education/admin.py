from django.contrib import admin

from .forms import MinOneForm
from .models import (Language, Profile, School, Favourites_School, 
                     Sport, Create, Intelligence, Music, Kindergartens, 
                     Favourites_Kindergartens, Course, Favourites_Course)

#Школа
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
    list_display = ('name', 'album', 'description',
                    'telephone', 'address', 'price', 'price_of_year', 
                    'email', 'classes', 'name_author', 'underground', 
                    'area', 'age')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]


class Favourites_SchoolAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user',]


#Детский сад
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
    list_display = ('name', 'album', 'description',
                    'telephone', 'address', 'price', 
                    'email', 'underground', 
                    'area', 'age', 'price_of_year', 'working_hours', 'group_suze')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]


class Favourites_KindergartensAdmin(admin.ModelAdmin):
    list_display = ('user', 'kindergartens')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user',]

#Курсы
Course
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'description',
                    'telephone', 'address', 'price', 
                    'email', 'underground', 
                    'area', 'age')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]


class Favourites_CourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user',]

admin.site.register(Language, LanguageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Create, CreateAdmin)
admin.site.register(Intelligence, IntelligenceAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Kindergartens, KindergartensAdmin)
admin.site.register(Favourites_School, Favourites_SchoolAdmin)
admin.site.register(Favourites_Kindergartens, Favourites_KindergartensAdmin)
admin.site.register(Favourites_Course, Favourites_CourseAdmin)


'''
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'default', 'album')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]

class ImageAlbumAdmin(admin.ModelAdmin):
    list_display = ('name',)
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name',]


class Favourites_educationAdmin(admin.ModelAdmin):
    list_display = ('user', 'education')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'
    ordering = ['user',]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]


class Educational_formAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name',]


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('role', 'image', 'first_name', 'last_name', 
                    'patronymic', 'experience', 'price_min', 'price_max', 
                    'achievement')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('first_name', 'last_name',)
    empty_value_display = '-пусто-'
    ordering = ['last_name',]


class Favourites_specialistAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialist')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'
    ordering = ['user',]
'''



'''

admin.site.register(Favourites_School, Favourites_educationAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Educational_form, Educational_formAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Favourites_specialist, Favourites_specialistAdmin)
'''