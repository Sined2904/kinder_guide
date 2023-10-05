from django.contrib.auth import get_user_model
from django.db import models


# Page is a temporary placeholder for the edu model's name
class Comment(models.Model):
    comment_post = models.ForeignKey(
        'education.Education',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    content = models.TextField()
    date_posted = models.DateTimeField(
        auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies',
    )

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'{self.author}: {self.content}'

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-id')

    @property
    def is_parent(self):
        return self.parent is None
