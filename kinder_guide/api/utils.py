from django.db.models import Avg


def get_avg_rating(model, obj):
    rating = model.objects.filter(review_post=obj.id).aggregate(Avg('rating'))
    if not rating['rating__avg']:
        return rating['rating__avg']
    return round(rating['rating__avg'], 1)
