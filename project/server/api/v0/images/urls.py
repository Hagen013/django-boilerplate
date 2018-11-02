from rest_framework.routers import DefaultRouter
from .views import OfferImageViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'', OfferImageViewSet, base_name="images")
urlpatterns = router.urls
