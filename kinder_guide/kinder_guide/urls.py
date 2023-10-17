from django.views.generic import TemplateView

from django.urls import path, include
from news.feeds import LatestNewsFeed

urlpatterns = [
    path('api/v1/', include('api.urls', namespace='api')),
    path('feed/', LatestNewsFeed(), name = 'news_feed'),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
