from .views import (
	CheckRefreshTokenWC,
	CheckRefreshTokenWRT,
	RefreshAccessTokenWRT,
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
		CheckRefreshTokenWC.as_view(),
		name="check_wc",
	),
	
	path(
		'api/check-wrt',
		CheckRefreshTokenWRT.as_view(),
		name="check_wrt",
	),

	path(
		'api/refresh-wrt',
		RefreshAccessTokenWRT.as_view(),
		name="refresh_wrt",
	),
]