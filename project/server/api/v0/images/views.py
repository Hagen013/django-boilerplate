from rest_framework.pagination import LimitOffsetPagination

from api.views import ModelViewSet
from shop.models import OfferImage
from shop.serializers import OfferImageSerializer


class OfferImageViewSet(ModelViewSet):

    model = OfferImage
    queryset = OfferImage.objects.all()
    serializer_class = OfferImageSerializer
    pagination_class = LimitOffsetPagination
