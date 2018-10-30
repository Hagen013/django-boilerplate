from django.urls import path, include

from .views import RegistrationAPIView, LoginAPIView


app_name = "api"

urlpatterns = [
    path('', RegistrationAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
]
