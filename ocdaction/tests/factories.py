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
            'obsession',
            'compulsion',
            'exposure'
        )

    challenge_name = 'challengename'
    is_archived = False
    obsession = 'obsession'
    compulsion = 'compulsion'
    exposure = 'exposure'
    user = factory.SubFactory(UserFactory)
