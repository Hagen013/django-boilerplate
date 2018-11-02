from django.db import models
from django.contrib.postgres.fields import JSONField

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from transliterate import translit

from .db import (Displayable,
                 Indexable,
                 Describable,
                 TimeStamped,
                 Sortable,
                 Image,
                 Named)

from .db.fields import PriceField


class WebPage(
        Displayable,
        Indexable,
        Describable,
        TimeStamped
    ):
    
    class Meta:
        abstract = True


class Offer(Named, Sortable):

    price = PriceField()

    old_price = PriceField()

    code = models.CharField(
        verbose_name="vendor code",
        max_length=128,
        db_index=True,
        unique=True
    )

    is_in_stock = models.BooleanField(
        verbose_name="is in stock",
        default=True
    )

    is_new = models.BooleanField(
        verbose_name="is new",
        default=False
    )

    is_bestseller = models.BooleanField(
        verbose_name="is bestseller",
        default=False
    )

    display_sale = models.BooleanField(
        verbose_name="display sale",
        default=True
    )

    display_in_selections = models.BooleanField(
        default=False
    )

    amount = models.PositiveIntegerField(
        verbose_name="amount in storage",
        default=0
    )
    
    attributes = JSONField(
        blank=True
    )

    class Meta:
        abstract = True

    @property
    def discount_amount(self):
        if self.price < self.old_price:
            return int(self.price - self.old_price)
        else:
            return 0


class AbstractOfferPage(Offer, WebPage):

    category_relation_class = None

    def add_category(self, category):
        return None

    def remove_category(self, category):
        return None

    def contains_category(self, category):
        return None

    def __repr__(self):
        return 'OfferPage: %s' % self.name

    def __str__(self):
        return '%s' % self.name

    class Meta:
        abstract = True


class Category(MPTTModel, Named, Sortable):

    parent = TreeForeignKey(
        "self",
        verbose_name="parent",
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class AbstractCategoryPage(Category, WebPage):

    def __repr__(self):
        return 'CategoryPage: %s' % self.name

    def __str__(self):
        return '%s' % self.name

    class Meta:
        abstract = True


class AbstractOfferImage(Image, Sortable, Describable, TimeStamped):

    offer = None

    upload_image_to = 'images/'
    image_key_attribute = 'name'

    @property
    def name(self):
        return translit(self.offer.name, 'ru', reversed=True).replace(' ', '-')

    class Meta:
        abstract = True
