"""
WSGI config for ocdaction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

