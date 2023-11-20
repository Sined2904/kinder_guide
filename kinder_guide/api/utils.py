from django.db.models import Avg
from geopy.geocoders import Nominatim


def get_avg_rating(model, obj):
    rating = model.objects.filter(review_post=obj.id).aggregate(Avg('rating'))
    if not rating['rating__avg']:
        return rating['rating__avg']
    return round(rating['rating__avg'], 1)


def get_coordinates_from_address(self):
    address = self.address
    geolocator = Nominatim(user_agent="Tester")
    location = geolocator.geocode(address)
    coordinates = [location.latitude, location.longitude]
    return coordinates
