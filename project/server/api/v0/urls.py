from django.urls import path, include


app_name = "api"

urlpatterns = [
    path("auth/", include("api.v0.auth.urls", namespace="auth")),
    path("users/", include("api.v0.users.urls", namespace="users")),
    path("jwt/", include("api.v0.jwt.urls", namespace="jwt")),
    path("categories/", include("api.v0.categories.urls", namespace="categories")),
    path("offers/", include("api.v0.offers.urls", namespace="offers"))
]
