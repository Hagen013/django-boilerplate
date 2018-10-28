from django.db import models
from django.core.validators import validate_slug


class DisplayableURLField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs["verbose_name"] = "URL"
        kwargs["max_length"] = 2048
        kwargs["editable"] = False
        kwargs["unique"] = True
        kwargs["validators"] = [
                validate_slug
            ]
        super(DisplayableURLField, self).__init__(*args, **kwargs)
