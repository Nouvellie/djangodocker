from django.contrib import admin
from django.urls import (
    include, 
    path,
)


django_urls = [
    path('admin/', admin.site.urls),
]

apps_urls = [
    path(
        '',
        include('apps.core.urls'),
    ),
]

urlpatterns = django_urls + apps_urls