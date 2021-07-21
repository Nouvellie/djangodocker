from .views import StartAPIView
from django.urls import path


urlpatterns = [
	path(
		'',
		StartAPIView.as_view(),
		name="start",
	),
]