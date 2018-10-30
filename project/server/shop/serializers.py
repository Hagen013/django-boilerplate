from rest_framework import serializers

from core.serializers import DynamicFieldsModelSerializer

from .models import CategoryPage, OfferPage


class BaseCategorySerializer(DynamicFieldsModelSerializer):

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
        fields = (
            'id',
            'name',
            'url',
            'slug',
            'is_published',
            'is_bestseller'
        )
        read_only_fields = (
            'id',
        )


class ImageSerializer(serializers.ModelSerializer):
    pass

