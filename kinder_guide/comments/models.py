from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from education.models import School, Kindergartens


class Review(models.Model):

    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(
        auto_now_add=True)
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'{self.author}: {self.content}'


class ReviewSchool(Review):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    review_post = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        verbose_name = 'Отзыв школы'
        verbose_name_plural = 'Отзывы школ'
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'review_post'],
                name='unique_author_reviewschool'
            ),
        )


class ReviewKindergarten(Review):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    review_post = models.ForeignKey(
        Kindergartens,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        verbose_name = 'Отзыв детского сада'
        verbose_name_plural = 'Отзывы детских садов'
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'review_post'],
                name='unique_author_reviewkindergarten'
            ),
        )
