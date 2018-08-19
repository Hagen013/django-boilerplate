from .base import *


# BASIC CONFIGURATION START
# ------------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ["*"]
# ------------------------------------------------------------------------------
# BASIC CONFIGURATION END


# DATABASE CONFIGURATION START
# ------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(ROOT_DIR.path("server/db.sqlite3"))
    }
}
# ------------------------------------------------------------------------------
# DATABASE CONFIGURATION END
