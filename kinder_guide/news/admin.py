from django.contrib import admin


@admin.register
class News(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'content',
        'date_posted'
    )
    list_filter = (
        'date_posted'
    )
