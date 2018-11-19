from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from api.views import ModelViewSet
from shop.models import CategoryPage
from shop.serializers import CategoryPlainSerializer, CategoryTreeSerializer


class CategoryPageViewSet(ModelViewSet):

    model = CategoryPage
    queryset = CategoryPage.objects.all()
    serializer_class = CategoryPlainSerializer
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
