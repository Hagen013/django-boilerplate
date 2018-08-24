from django.db import models


class Describable(models.Model):

    class Meta:
        abstract = True

    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
    