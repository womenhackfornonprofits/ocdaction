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

class AnxietyScore(models.Model):
    ZERO = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'

    ANXIETY_SCORE_CHOICES = (
        (ZERO, 'Zero'),
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
        (FIVE, 'Five'),
        (SIX, 'Six'),
        (SEVEN, 'Seven'),
        (EIGHT, 'Eight'),
        (NINE, 'Nine'),
        (TEN, 'Ten'),
    )
    score = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        default=ZERO
    )
    user = models.ForeignKey('profiles.OCDActionUser', on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)

