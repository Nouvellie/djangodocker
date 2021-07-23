from .models import VerifiedAccount
from .serializers import (
	MyTokenObtainPairSerializer, 
	VerifiedAccountSerializer,
)
from datetime import (
	datetime, 
	timezone,
)
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.shortcuts import render
from django.views.generic import TemplateView
from djangodocker.settings import (
	DEBUG, 
	info,
)
from rest_framework import (
	generics,
	status,
)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_400_BAD_REQUEST,
	HTTP_401_UNAUTHORIZED,
	HTTP_404_NOT_FOUND,
	HTTP_426_UPGRADE_REQUIRED,
)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken as RT
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken as OT

import re
import time
import traceback


class StartAPI(APIView):

	permission_classes = (IsAuthenticated,)
	
	def get(self, request, format=None):
		testing_data = 'Start API View testing..'

		return Response(testing_data, status=HTTP_200_OK)


class SignInView(TokenObtainPairView):
	"""
	Login View with jWt token authentication
	"""
	serializer_class = MyTokenObtainPairSerializer

class SignIn(APIView):

	def post(self, request, format=None):
		try:
			username = request.data.get('username')
			password = request.data.get('password')
			authenticated_user = authenticate(username=username, password=password)
			
			if authenticated_user:
				OT.objects.filter(user_id=authenticated_user).delete()
				JWT_TOKEN = RT.for_user(authenticated_user)

				output = {
					'refresh': str(JWT_TOKEN),
					'access': str(JWT_TOKEN.access_token),
				}
				
				update_last_login(None, authenticated_user)
				return Response(output, status=HTTP_200_OK)
			else:
				return Response({"error": "Invalid credentials."}, status=HTTP_401_UNAUTHORIZED)

		except:
			return Response({"error": "An error occurred, please try again."}, status=HTTP_400_BAD_REQUEST)


class CheckRefreshTokenWC(APIView):

	def get(self, request, format=None):
		try:
			username = request.data.get('username')
			password = request.data.get('password')
			authenticated_user = authenticate(username=username, password=password)

			if authenticated_user:
				JWT_TOKEN = OT.objects.filter(user_id=authenticated_user).latest('id')				
				
				output = {
					'refresh': str(JWT_TOKEN.token),
					'created': str(JWT_TOKEN.created_at),
					'expires': str(JWT_TOKEN.expires_at),
					'expired': True if datetime.now(timezone.utc) >= JWT_TOKEN.expires_at else False,
				}

				return Response(output, status=HTTP_200_OK)
			
			else:
				return Response({'error': 'Invalid credentials.'}, status=HTTP_401_UNAUTHORIZED)	

		except:
			return Response({"error": "An error occurred, please try again."}, status=HTTP_400_BAD_REQUEST)


class CheckRefreshTokenWRT(APIView):

	def get(self, request, format=None):
		try:
			refresh = request.data.get('refresh')
			
			JWT_TOKEN = OT.objects.filter(token=refresh).latest('id')
			
			output = {
				'refresh': str(JWT_TOKEN.token),
				'created': str(JWT_TOKEN.created_at),
				'expires': str(JWT_TOKEN.expires_at),
				'expired': True if datetime.now(timezone.utc) >= JWT_TOKEN.expires_at else False,
			}

			return Response(output, status=HTTP_200_OK)

		except:
			return Response({"error": "Check the refresh token please."}, status=HTTP_400_BAD_REQUEST)

class SignInView(TokenObtainPairView):
	"""
	Login View with jWt token authentication
	"""
	serializer_class = MyTokenObtainPairSerializer
	def get(self, request, format=None):
		try:
			refresh = request.data.get('refresh')
			token_user = OT.objects.get(token=refresh)
			
			output = {
				'refresh': str(token_user.token),
				'access': str(RT(token=token_user.token).access_token),
				'created': str(token_user.created_at),
				'expires': str(token_user.expires_at),
				'expired': True if datetime.now(timezone.utc) >= token_user.expires_at else False,
			}

			return Response(output, status=HTTP_200_OK)

		except:
			return Response({"error": "Check the refresh token please."}, status=HTTP_400_BAD_REQUEST)


class RefreshAccessTokenWRT(APIView):

	def get(self, request, format=None):
		try:
			refresh = request.data.get('refresh')
			token_user = OT.objects.get(token=refresh)
			
			output = {
				'refresh': str(token_user.token),
				'access': str(RT(token=token_user.token).access_token),
				'created': str(token_user.created_at),
				'expires': str(token_user.expires_at),
				'expired': True if datetime.now(timezone.utc) >= token_user.expires_at else False,
			}

			return Response(output, status=HTTP_200_OK)

		except:
			return Response({"error": "Check the refresh token please."}, status=HTTP_400_BAD_REQUEST)
			

class ListVerifyAccountCreated(generics.ListAPIView):
	queryset = VerifiedAccount.objects.all()
	serializer_class = VerifiedAccountSerializer