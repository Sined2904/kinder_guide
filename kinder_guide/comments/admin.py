from django.contrib import admin


@admin.register
class Comment(admin.ModelAdmin):
    list_display = (
        'comment_post',
        'author',
        'content',
        'date_posted',
        'parent'
    )
    list_filter = (
        'parent',
        'date_posted'
    )
    search_fields = (
        'author',
        'content',
        'date_posted'
    )
