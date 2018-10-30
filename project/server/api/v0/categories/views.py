from rest_framework.pagination import LimitOffsetPagination

from api.views import ModelViewSet
from shop.models import CategoryPage
from shop.serializers import CategoryPlainSerializer, CategoryTreeSerializer


class CategoryPageViewSet(ModelViewSet):

    model = CategoryPage
    queryset = CategoryPage.objects.all()
    serializer_class = CategoryPlainSerializer
    pagination_class = LimitOffsetPagination
    