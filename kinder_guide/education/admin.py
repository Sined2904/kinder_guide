from django.contrib import admin

# from .forms import MinOneForm
from .models import (AgeCategory, Area, Create, Favourites_Kindergartens,
                     Favourites_School, Intelligence, KindergartenAlbum,
                     Kindergartens, Language, Music, Profile, School,
                     SchoolAlbum, Sport, Underground)


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
    list_display = ('category',)
    search_fields = ('category', )


# школа
class SchoolAlbumInline(admin.TabularInline):
    model = SchoolAlbum


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'telephone',
                    'address', 'price', 'price_of_year', 'email',
                    'classes', 'area', 'age', 'working_hours')
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
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class CreateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class IntelligenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]


class KindergartenAlbumInline(admin.TabularInline):
    model = KindergartenAlbum


class KindergartensAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',
                    'telephone', 'address', 'price',
                    'email', 'area', 'age',
                    'price_of_year', 'working_hours', 'group_suze')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    ordering = ['name', ]
    inlines = [KindergartenAlbumInline, ]


class Favourites_KindergartensAdmin(admin.ModelAdmin):
    list_display = ('user', 'kindergartens')
    empty_value_display = '-пусто-'
    search_fields = ('user', )
    ordering = ['user', ]


admin.site.register(Underground, UndergroundAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AgeCategory, AgeCategoryAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Create, CreateAdmin)
admin.site.register(Intelligence, IntelligenceAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Kindergartens, KindergartensAdmin)
admin.site.register(Favourites_School, Favourites_SchoolAdmin)
admin.site.register(Favourites_Kindergartens, Favourites_KindergartensAdmin)
