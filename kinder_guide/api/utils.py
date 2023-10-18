from django.db.models import Avg
from comments.models import Review


def get_avg_rating():
    rating = Review.objects.all().aggregate(Avg('rating'))
    return rating['rating__avg']
