from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/", include("api.urls", namespace="api")),
    path("u/", include("users.urls", namespace="users")),
    path("admin/", TemplateView.as_view(template_name="admin.html"))
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
