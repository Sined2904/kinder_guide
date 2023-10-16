from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    content = models.TextField()
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
    review_post = models.ForeignKey(
        'education.School',
        on_delete=models.CASCADE,
        related_name='reviews'
    )


class ReviewCourse(Review):
    review_post = models.ForeignKey(
        'education.Course',
        on_delete=models.CASCADE,
        related_name='reviews'
    )


class ReviewKindergarten(Review):
    review_post = models.ForeignKey(
        'education.Kindergartens',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
