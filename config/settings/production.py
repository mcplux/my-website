from .base import *  # noqa

DEBUG = False

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"]["BACKEND"] = (  # noqa
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
)

ALLOWED_HOSTS = ["*"]

try:
    from .local import *  # noqa
except ImportError:
    pass
