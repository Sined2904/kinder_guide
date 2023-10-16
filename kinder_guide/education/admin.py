from django.contrib import admin

from .forms import MinOneForm
from .models import (Language, Profile, School)


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


admin.site.register(Language, LanguageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(School, SchoolAdmin)

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

admin.site.register(Favourites_education, Favourites_educationAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Educational_form, Educational_formAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Favourites_specialist, Favourites_specialistAdmin)
'''