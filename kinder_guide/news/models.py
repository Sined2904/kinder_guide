from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


class News(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.content
