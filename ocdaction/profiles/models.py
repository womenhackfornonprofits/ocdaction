from __future__ import unicode_literals

from django.db import models
from custom_user.models import AbstractEmailUser
import datetime

class OCDActionUser(AbstractEmailUser):

    # basic info
    username = models.CharField(max_length=24, blank=True)
    date_birth = models.DateField('date of birth')
    def is_date_of_birth_valid(self):
        today = datetime.date.today()
        if self.date_birth > today:
            return False
