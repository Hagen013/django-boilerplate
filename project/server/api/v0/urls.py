from django.urls import path, include


app_name = "api"

urlpatterns = [
    path("users/", include("api.v0.users.urls", namespace="users")),
]
