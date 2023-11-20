from django.db.models import Avg
from geopy.geocoders import Nominatim


def get_avg_rating(model, obj):
    rating = model.objects.filter(review_post=obj.id).aggregate(Avg('rating'))
    if not rating['rating__avg']:
        return rating['rating__avg']
    return round(rating['rating__avg'], 1)


def get_coordinates_from_address(self):
    geolocator = Nominatim(user_agent="Tester")
    location = geolocator.geocode(self.address)
    if location:
        self.latitude = location.latitude
        self.longitude = location.longitude
