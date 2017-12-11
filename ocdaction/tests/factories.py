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

    username = factory.Sequence(lambda n: 'username_{}'.format(n))
    date_birth = datetime.date(2000, 1, 2)
    have_ocd = True
    email = factory.Sequence(lambda n: 'email_{}'.format(n))


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

    challenge_name = factory.Sequence(lambda n: 'challengename_{}'.format(n))
    is_archived = False
    in_progress = False
    obsession = 'obsession'
    compulsion = 'compulsion'
    exposure = 'exposure'
    user = factory.SubFactory(UserFactory)
