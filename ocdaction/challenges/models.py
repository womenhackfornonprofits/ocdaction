from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models, transaction


class Challenge(models.Model):
    """a challenge is a user created challenge that can be completed
    by a user to track anxiety
    """
    challenge_name = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    obsession = models.CharField(max_length=300, blank=True)
    compulsion = models.CharField(max_length=300, blank=True)
    exposure = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey('profiles.OCDActionUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.challenge_name

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.in_progress:
            Challenge.objects.filter(in_progress=True).update(in_progress=False)
        super(Challenge, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('challenge-edit',
                       kwargs={'challenge_id': self.id})

    def archive(self):
        self.is_archived = True
        self.save()

    def get_latest_initial_anxiety_level(self):
        try:
            anxiety_score_card = AnxietyScoreCard.objects.filter(challenge=self).last()
            latest_initial_anxiety_level = anxiety_score_card.anxiety_at_0_min
        except:
            AnxietyScoreCard.DoesNotExist
            latest_initial_anxiety_level = "-"
        return latest_initial_anxiety_level


class AnxietyScoreCard(models.Model):
    """
    Anxiety score card is a collection of scores for the challenge
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
        (SCORE_ZERO, 'zero'),
        (SCORE_ONE, 'one'),
        (SCORE_TWO, 'two'),
        (SCORE_THREE, 'three'),
        (SCORE_FOUR, 'four'),
        (SCORE_FIVE, 'five'),
        (SCORE_SIX, 'six'),
        (SCORE_SEVEN, 'seven'),
        (SCORE_EIGHT, 'eight'),
        (SCORE_NINE, 'nine'),
        (SCORE_TEN, 'ten'),
    )

    anxiety_at_0_min = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        blank=False
    )
    anxiety_at_5_min = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        blank=True
    )
    anxiety_at_10_min = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        blank=True
    )
    anxiety_at_15_min = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        blank=True
    )
    anxiety_at_30_min = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        blank=True
    )
    anxiety_at_60_min = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        blank=True
    )
    anxiety_at_120_min = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        blank=False
    )
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)

    def user_name(self):
        return self.challenge.user

    def get_absolute_url(self):
        return reverse(
            'challenge-score-form',
            kwargs={'challenge_id': self.challenge.id})

    def get_score_url(self):
        return reverse(
            'challenge-summary',
            kwargs={'challenge_id': self.challenge.id,
                    'score_id': self.id})
