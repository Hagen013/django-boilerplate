from datetime import datetime

from django.contrib.auth import login, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_response_payload_handler


class ObtainTokenAPIView(JSONWebTokenAPIView):
    """
    Overriding post method for session-based authentication support
    """
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            login(request, user)
            print(user)
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (
                    datetime.utcnow() +
                    api_settings.JWT_EXPIRATION_DELTA
                )
                response.set_cookie(
                    api_settings.JWT_AUTH_COOKIE,
                    token,
                    expires=expiration,
                    httponly=True
                )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

obtain_jwt_token = ObtainTokenAPIView.as_view()