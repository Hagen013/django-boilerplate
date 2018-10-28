from django.db import models


class Named(models.Model):

    name = models.CharField(
        max_length=1024,
        verbose_name="name",
        db_index=True
    )

    class Meta:
        abstract = True
