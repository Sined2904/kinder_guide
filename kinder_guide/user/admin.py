from django.contrib import admin

from .models import MyUser


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'first_name',
        'last_name',
        'phone',
        'child_first_name',
        'child_last_name',
    )
    search_fields = ('email',)
    list_filter = ('email',)
    empty_value_display = '-пусто-'
