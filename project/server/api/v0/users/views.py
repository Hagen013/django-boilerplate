from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserSerializer


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

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


