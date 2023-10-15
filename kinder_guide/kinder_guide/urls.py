from django.contrib import admin
from django.views.generic import TemplateView

from django.urls import path, include
from news.feeds import LatestNewsFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('feed/', LatestNewsFeed(), name = 'news_feed'),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
