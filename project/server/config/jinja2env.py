import json

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from urllib.parse import urlencode

from jinja2 import Environment


def url_replace(querystring, kwargs):
    query = querystring.dict()
    query.update(kwargs)
    return urlencode(query)


def to_json(value):
    return json.dumps(value)


def escape_quotes(value):
    return value.replace("'", "")


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'url_replace': url_replace,
        'to_json': to_json,
        'escape_quotes': escape_quotes
    })
    return env