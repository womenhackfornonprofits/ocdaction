import factory.django

from profiles.models import OCDActionUser
from challenges.models import Challenge
import datetime


# Factories
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OCDActionUser
        django_get_or_create = (
            'username',
            'date_birth',
            'have_ocd'
        )

    username = 'testuser'
    date_birth = datetime.date(2000, 1, 2)
    have_ocd = True


class ChallengeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Challenge
        django_get_or_create = (
            'challenge_name',
            'is_archived',
            'challenge_fears',
            'challenge_compulsions',
            'challenge_goals'
        )

    challenge_name = 'challengename'
    is_archived = False
    challenge_fears = 'fears'
    challenge_compulsions = 'compulsions'
    challenge_goals = 'goals'
    user = factory.SubFactory(UserFactory)
