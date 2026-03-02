import os
from .base import *  # noqa

DEBUG = False

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
# STORAGES["staticfiles"]["BACKEND"] = (  # noqa
#     "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
# )
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
ALLOWED_HOSTS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")


try:
    from .local import *  # noqa
except ImportError:
    pass
