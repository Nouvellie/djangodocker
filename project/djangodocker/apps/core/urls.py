from .views import (
	CheckTokenWC,
	CheckTokenWR,
	StartAPI, 
	SignIn,
)
from django.urls import path


urlpatterns = [
	path(
		'',
		StartAPI.as_view(),
		name="start",
	),

	path(
		'api/signin',
		SignIn.as_view(),
		name="signin",
	),

	path(
		'api/check-wc',
		CheckTokenWC.as_view(),
		name="check_wc",
	),
	
	path(
		'api/check-wr',
		CheckTokenWR.as_view(),
		name="check_wr",
	),
]