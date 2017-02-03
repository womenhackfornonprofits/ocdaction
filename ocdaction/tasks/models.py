from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    """a task is a user created task that can be completed
    by a user to track anxiety
    """
    taskname = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)
    task_fears = models.CharField(max_length=300, blank=True)
    task_compulsions = models.CharField(max_length=300, blank=True)
    task_goals = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey('profiles.OCDActionUser', on_delete=models.CASCADE)

    # TODO add a task anxiety score once score model is created

    def __str__(self):
        return self.taskname