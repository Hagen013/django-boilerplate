from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager

from .db import Displayable, Indexable, Describable
from .db.fields import PriceField


class WebPage(
        Displayable,
        Indexable,
        Describable
    ):
    
    class Meta:
        abstract = True


class Offer(models.Model):

    price = PriceField()

    old_price = PriceField()

    code = models.CharField(
        verbose_name="vendor code",
        max_length=128,
        db_index=True
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
        verbose_name="display sale"
        default=True
    )

    amount = models.PositiveIntegerField(
        verbose_name="amount"
    )

    @property
    def discount_amount(self):
        if self.price < self.old_price:
            return int(self.price - self.old_price)
        else:
            return 0


class OfferPage(WebPage):

    class Meta:
        abstract = True


class CategoryPage(MPTTModel, WebPage):

    class Meta:
        abstract = True

    parent = TreeForeignKey(
        "self",
        verbose_name="parent",
        null=True,
        db_index=True,
        on_delete=models.CASCADE
    )


