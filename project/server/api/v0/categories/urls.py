from rest_framework.routers import DefaultRouter
from .views import CategoryPageViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'', CategoryPageViewSet, base_name="categories")
urlpatterns = router.urls
