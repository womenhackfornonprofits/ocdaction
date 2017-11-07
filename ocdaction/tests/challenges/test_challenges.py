import pytest

from tests.factories import UserFactory, ChallengeFactory
from challenges.models import Challenge


@pytest.mark.django_db
def test_create_challenge():

    user = UserFactory.create()

    # Check there are 0 challenges before a new challenge is added
    number_challenges = Challenge.objects.filter(user_id=user.id).count()
    assert number_challenges == 0

    challenge = ChallengeFactory.create()

    # Check there is 1 challenge after a new challenge is added
    # and that it's not archived
    number_challenges = Challenge.objects.filter(user_id=user.id).count()
    challenge = Challenge.objects.get(user_id=user.id)
    assert number_challenges == 1
    assert challenge.is_archived is False


@pytest.mark.django_db
def test_archive_challenge():

    user = UserFactory.create()
    challenge = ChallengeFactory.create()

    challenge.archive()
    assert challenge.is_archived is True
