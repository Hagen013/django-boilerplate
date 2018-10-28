from django.db import models


class Sortable(models.Model):

    class Meta:
        abstract = True

    order = models.IntegerField(
        verbose_name='order',
        default=0,
    )
