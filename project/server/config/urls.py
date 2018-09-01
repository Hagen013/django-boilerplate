from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/", include("api.urls", namespace="api")),
    path("u/", include("users.urls", namespace="users"))
]

