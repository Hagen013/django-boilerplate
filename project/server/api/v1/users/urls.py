from django.urls import path, include

from .views import UserListAPIView


app_name = "api"

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
]
