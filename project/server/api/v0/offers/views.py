from rest_framework.pagination import LimitOffsetPagination

from api.views import ModelViewSet
from shop.models import OfferPage
from shop.serializers import OfferSerializer


class OfferPageViewSet(ModelViewSet):

    model = OfferPage
    serializer_class = OfferSerializer
    pagination_class = LimitOffsetPagination
