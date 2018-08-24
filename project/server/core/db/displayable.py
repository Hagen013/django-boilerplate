from django.db import models
from django.core.validators import RegexValidator

from .fields import DisplayableURLField


class DisplayableManager(models.Manager):

    def get_queryset(self):
        return super(DisplayableManager, self).get_queryset().\
            filter(is_published=True).\
            order_by('-scoring')


class Displayable(models.Model):

    class Meta:
        abstract = True

    objects = models.Manager()
    public = DisplayableManager()

    # Adresses fields
    slug = DisplayableURLField()
    url = DisplayableURLField()

    def get_absolute_url(self):
        msg = "Method get_absolute_url() must be implemented by subclass: `{}`"
        raise NotImplementedError(msg.format(self.__class__.__name__))

    @property
    def absolute_url(self):
        return self.get_absolute_url()

    scoring = models.IntegerField(
        verbose_name='scoring',
        default=0,
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='published'
    )

    def save(self, *args, **kwargs):
        super(Displayable, self).save(*args, **kwargs)

