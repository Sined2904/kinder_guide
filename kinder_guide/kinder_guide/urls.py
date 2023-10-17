from django.views.generic import TemplateView
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api.urls', namespace='api')),
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
