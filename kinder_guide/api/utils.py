from django.db.models import Avg

from comments.models import ReviewCourse


def get_avg_rating(model):
    rating = model.objects.all().aggregate(Avg('rating'))
    return rating['rating__avg']

def get_avg_rating_course(course):
    reviews = ReviewCourse.objects.filter(review_post=course)
    avg_rating = reviews.aggregate(Avg('rating'))
    return avg_rating['rating__avg'] or 0
