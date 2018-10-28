from django.db import models


class Indexable(models.Model):

    class Meta:
        abstract = True

    _title = models.CharField(
        blank=True,
        verbose_name='H1 title',
        max_length=512
    )

    _meta_title = models.CharField(
        blank=True,
        verbose_name='meta-tag title',
        max_length=512
    )

    _meta_keywords = models.CharField(
        blank=True,
        verbose_name='meta-tag keywords',
        max_length=512
    )

    _meta_description = models.CharField(
        blank=True,
        verbose_name='meta-tag description',
        max_length=512
    )

    def get_meta_title(self):
        return self._title

    def get_meta_keywords(self):
        return self._meta_keywords

    def get_meta_description(self):
        return self._meta_description

    def get_title(self):
        return self._title

    @property
    def title(self):
        return self._title

    @property
    def meta_title(self):
        return self.get_meta_title()

    @property
    def meta_keywords(self):
        return self.get_meta_keywords()

    @property
    def meta_description(self):
        return self.get_meta_description()

