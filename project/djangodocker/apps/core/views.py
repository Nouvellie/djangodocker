from datetime import (
	datetime, 
	timezone,
)
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.generic import TemplateView
from djangodocker.settings import DEBUG, info
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


class SignIn(APIView):

	def post(self, request, format=None):
		try:
			username = request.data.get('username')
			password = request.data.get('password')
			authenticated_user = authenticate(username=username, password=password)
			
			if authenticated_user:
				JWT_TOKEN = RT.for_user(authenticated_user)

				output = {
					'refresh': str(JWT_TOKEN),
					'access': str(JWT_TOKEN.access_token),
				}
				
				return Response(output, status=HTTP_200_OK)
			else:
				return Response({"error": "Invalid credentials."}, status=HTTP_401_UNAUTHORIZED)

		except:
			return Response({"error": "An error occurred, please try again."}, status=HTTP_400_BAD_REQUEST)


class CheckTokenWC(APIView):

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


class CheckTokenWR(APIView):

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
			# full_traceback = {'error': re.sub(r"\n\s*", " || ", traceback.format_exc())}
			# return Response(full_traceback, status=HTTP_400_BAD_REQUEST)
			return Response({"error": "Check the token please."}, status=HTTP_400_BAD_REQUEST)


