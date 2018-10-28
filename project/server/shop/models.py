from django.db import models

from core.models import (AbstractCategoryPage,
                        AbstractOfferPage,)


class Product(models.Model):

    class Meta:
        abstract = False


class CategoryPage(AbstractCategoryPage):

    class Meta:
        abstract = False


class OfferPageCategoryRelation(models.Model):

    unique_together = (("offer", "category"))

    offer = models.ForeignKey(
        "OfferPage",
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        "CategoryPage",
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = False


class OfferPage(AbstractOfferPage):

    category_relation_class = OfferPageCategoryRelation

    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        related_name="offers",
        blank=True,
        null=True
    )

    categories = models.ManyToManyField(
        "CategoryPage",
        related_name="products",
        through=category_relation_class,
    )

    class Meta:
        abstract = False

