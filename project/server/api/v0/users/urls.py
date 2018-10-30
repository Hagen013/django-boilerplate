from django.urls import path, include

from .views import UserListAPIView, UserInfoAPIView


app_name = "api"

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('info/', UserInfoAPIView.as_view(), name='info'),
]
