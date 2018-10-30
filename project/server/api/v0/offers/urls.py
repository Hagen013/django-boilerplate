from rest_framework.routers import DefaultRouter
from .views import OfferPageViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'', OfferPageViewSet, base_name="offers")
urlpatterns = router.urls
