from django.contrib import admin
from django.urls import (
    include, 
    path,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_registration.api.views import register as SignUp


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

    path(
        'accounts/', 
        include('rest_registration.api.urls'),
    ),
    path(
        'reg', 
        SignUp, 
        name='reg'
    ),
]

urlpatterns = django_urls + apps_urls + rest_urls