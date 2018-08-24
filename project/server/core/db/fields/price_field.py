from django.db import models
from django.core.validators import RegexValidator


class PriceField(models.DecimalField):

    def __init__(self, *args, **kwargs):
        kwargs["max_digits"] = 8
        kwargs["decimal_places"] = 2
        super(PriceField, self).__init__(*args, **kwargs)
