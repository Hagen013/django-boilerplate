from rest_framework import serializers

from core.serializers import DynamicFieldsModelSerializer

from .models import CategoryPage, OfferPage, OfferImage


class BaseCategorySerializer(DynamicFieldsModelSerializer):

    url = serializers.CharField(max_length=2048)
    slug = serializers.CharField(max_length=2048)

    class Meta:
        model = CategoryPage
        fields = (
            'id',
            '_title',
            'name',
            'url',
            'slug',
            'parent',
            'description',
            'is_published',
            'order',
            'scoring',
            'created_at',
            'modified_at',
            'level',
            '_meta_title',
            '_meta_keywords',
            '_meta_description'
        )
        read_only_fields = (
            'id',
            'level'
        )


class CategoryTreeSerializer(BaseCategorySerializer):
    
    class Meta(BaseCategorySerializer.Meta):
        pass


class CategoryPlainSerializer(BaseCategorySerializer):
    
    class Meta(BaseCategorySerializer.Meta):
        pass


class OfferSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = OfferPage
        fields = '__all__'
        read_only_fields = (
            'id',
        )


class OfferImageSerializer(serializers.ModelSerializer):

    thumbnail = serializers.ImageField(use_url=True, read_only=True)

    class Meta:
        model = OfferImage
        fields = '__all__'
        read_only_fields = (
            'id',
            'thumbnail',
        )
