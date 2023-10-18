from django.db.models import Avg


def get_avg_rating(model):
    rating = model.objects.all().aggregate(Avg('rating'))
    return rating['rating__avg']
