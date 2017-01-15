from __future__ import unicode_literals

from django.db import models
from custom_user.models import AbstractEmailUser


class OCDActionUser(AbstractEmailUser):

    # basic info
    username = models.CharField(max_length=24, blank=True)
    date_birth = models.DateField('date of birth', null=True, blank=True)
    have_ocd = models.BooleanField(default=True, blank=True)


class Task(models.Model):
    taskname = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey('OCDActionUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.taskname