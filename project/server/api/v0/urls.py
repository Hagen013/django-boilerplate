from django.urls import path, include


app_name = "api"

urlpatterns = [
    path("auth/", include("api.v0.auth.urls", namespace="auth")),
    path("users/", include("api.v0.users.urls", namespace="users"))
]
