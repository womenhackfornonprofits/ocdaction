from __future__ import unicode_literals
from django.db import models
from custom_user.models import AbstractEmailUser


class OCDActionUser(AbstractEmailUser):
    """ User is authenticated with their email
    but for app purposes users also have usernames.
    """
    username = models.CharField(max_length=24)
    date_birth = models.DateField('date of birth')
    have_ocd = models.BooleanField(default=False)

    def __str__(self):
        return self.username
