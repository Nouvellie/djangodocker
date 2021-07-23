from django.contrib import admin
from django.urls import (
    include, 
    path,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
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

rest_urls = [

    # path(
    #     'accounts/', 
    #     include('rest_registration.api.urls'),
    # ),
    
]

urlpatterns = django_urls + apps_urls