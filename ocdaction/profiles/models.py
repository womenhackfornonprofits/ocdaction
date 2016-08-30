from __future__ import unicode_literals

from django.db import models
from custom_user.models import AbstractEmailUser

class OCDActionUser(AbstractEmailUser):

    # basic info
    username = models.CharField(max_length=24, blank=True)
    