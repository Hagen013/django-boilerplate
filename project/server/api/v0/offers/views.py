from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from api.views import ModelViewSet
from shop.models import OfferPage
from shop.serializers import OfferSerializer


class OfferPageViewSet(ModelViewSet):

    model = OfferPage
    serializer_class = OfferSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )

    filter_fields = (
        'parent',
        'is_published',
    )
    search_fields = (
        'name',
    )
    ordering_fields = (
        'id',
        'scoring',
        'order',
        'level',
        'created_at',
        'modified_at'
    )
