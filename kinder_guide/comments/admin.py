from django.contrib import admin

from .models import ReviewSchool, ReviewKindergarten, ReviewCourse


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_post',
        'author',
        'content',
        'date_posted',
        'rating',
        'parent',
    )
    list_filter = (
        'parent',
        'date_posted',
        'rating',
    )
    search_fields = (
        'author',
        'content',
        'date_posted'
    )


admin.site.register(ReviewSchool, ReviewAdmin)
admin.site.register(ReviewKindergarten, ReviewAdmin)
admin.site.register(ReviewCourse, ReviewAdmin)
