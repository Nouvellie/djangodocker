from django.shortcuts import render
from django.views.generic import TemplateView
from djangodocker.settings import DEBUG, info
from rest_framework import (
	generics,
	status,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_400_BAD_REQUEST,
	HTTP_401_UNAUTHORIZED,
	HTTP_404_NOT_FOUND,
	HTTP_426_UPGRADE_REQUIRED,
)
from rest_framework.views import APIView

import re
import time
import traceback


class StartAPIView(APIView):

	permission_classes = (AllowAny,)
	
	def get(self, request, format=None):
		testing_data = 'Start API View testing..'

		return Response(testing_data, status=HTTP_200_OK)