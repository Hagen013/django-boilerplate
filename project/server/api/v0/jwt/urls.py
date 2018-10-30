from django.urls import path, include

from rest_framework_jwt.views import (refresh_jwt_token,
                                      verify_jwt_token)

from .views import obtain_jwt_token

app_name = "api"

urlpatterns = [
    path("obtain/", obtain_jwt_token, name="obtain"),
    path("verify/", verify_jwt_token, name="verify"),
    path("refresh/", refresh_jwt_token, name="refresh")
]
