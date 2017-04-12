from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models


class Task(models.Model):
    """a task is a user created task that can be completed
    by a user to track anxiety
    """
    task_name = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)
    task_fears = models.CharField(max_length=300, blank=True)
    task_compulsions = models.CharField(max_length=300, blank=True)
    task_goals = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey('profiles.OCDActionUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task-edit',
                       kwargs={'task_id': self.id})


class AnxietyScore(models.Model):
    """a task is a user created task that can be completed
    by a user to track anxiety
    """
    SCORE_ZERO = '0'
    SCORE_ONE = '1'
    SCORE_TWO = '2'
    SCORE_THREE = '3'
    SCORE_FOUR = '4'
    SCORE_FIVE = '5'
    SCORE_SIX = '6'
    SCORE_SEVEN = '7'
    SCORE_EIGHT = '8'
    SCORE_NINE = '9'
    SCORE_TEN = '10'

    ANXIETY_SCORE_CHOICES = (
        (SCORE_ZERO, 'Zero'),
        (SCORE_ONE, 'One'),
        (SCORE_TWO, 'Two'),
        (SCORE_THREE, 'Three'),
        (SCORE_FOUR, 'Four'),
        (SCORE_FIVE, 'Five'),
        (SCORE_SIX, 'Six'),
        (SCORE_SEVEN, 'Seven'),
        (SCORE_EIGHT, 'Eight'),
        (SCORE_NINE, 'Nine'),
        (SCORE_TEN, 'Ten'),
    )
    score = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        default=SCORE_ZERO
    )

    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.score

    def user_name(self):
        return self.task.user


class AnxietyScoreCard(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    score_after_0_min = models.ForeignKey(
        AnxietyScore,
        blank=True,
        null=True,
        related_name='score_0',
        on_delete=models.CASCADE
    )

    score_after_5_min = models.ForeignKey(
        AnxietyScore,
        blank=True,
        null=True,
        related_name='score_5',
        on_delete=models.CASCADE
    )
    score_after_10_min = models.ForeignKey(
        AnxietyScore,
        blank=True,
        null=True,
        related_name='score_10',
        on_delete=models.CASCADE
    )
    score_after_15_min = models.ForeignKey(
        AnxietyScore,
        blank=True,
        null=True,
        related_name='score_15',
        on_delete=models.CASCADE
    )
    score_after_30_min = models.ForeignKey(
        AnxietyScore,
        blank=True,
        null=True,
        related_name='score_30',
        on_delete=models.CASCADE
    )

    score_after_60_min = models.ForeignKey(
        AnxietyScore,
        blank=True,
        null=True,
        related_name='score_60',
        on_delete=models.CASCADE
    )

    def user_name(self):
        return self.task.user
