from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.serializers import UserSerializer

User = get_user_model()


class UserListAPIView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = (IsAdminUser,)
    

class UserAPIView(APIView):

    def get(self, request, pk):
        return Response({
        })

    def put(self, request, pk):
        return Response({
        })

    def delete(self, request, pk):
        return Response({
        })


class UserInfoAPIView(APIView):

    serializer_class = UserSerializer
    permissions = (IsAuthenticated,)

    def get(self, request):
        return Response({
            "username": "tsoy"
        })
