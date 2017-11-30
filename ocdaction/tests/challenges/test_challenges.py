import pytest

from tests.factories import UserFactory, ChallengeFactory
from challenges.models import Challenge, AnxietyScoreCard


@pytest.mark.django_db
def test_create_challenge():

    user = UserFactory.create()

    # Check there are 0 challenges before a new challenge is added
    number_challenges = Challenge.objects.filter(user_id=user.id).count()
    assert number_challenges == 0

    challenge = ChallengeFactory.create()

    # Check there is 1 challenge after a new challenge is added
    # and that it's not archived or in progress
    number_challenges = Challenge.objects.filter(user_id=user.id).count()
    challenge = Challenge.objects.get(user_id=user.id)
    assert number_challenges == 1
    assert challenge.is_archived is False
    assert challenge.in_progress is False


@pytest.mark.django_db
def test_archive_challenge():

    user = UserFactory.create()
    challenge = ChallengeFactory.create()

    # Check that the is_archived flag is set to true when the archive function is called
    challenge.archive()
    assert challenge.is_archived is True

@pytest.mark.django_db
def test_save_challenge():

    user = UserFactory.create()
    challenge = ChallengeFactory.create()

    # Check that on saving a challenge in_progress is set to False
    challenge.save()
    assert challenge.in_progress is False

'''
@pytest.mark.django_db
def test_mark_challenge_in_progress():

    user = UserFactory.create()
    challenge1 = ChallengeFactory.create()
    challenge2 = ChallengeFactory.create()

    # Check that on saving a challenge in_progress is set to False when there is already a challenge in progress
    challenge1.in_progress = True
    challenge1.save()
    #challenge2.in_progress = True
    challenge2.save()
    assert challenge1.in_progress is True
    assert challenge2.in_progress is False
'''

@pytest.mark.django_db
def test_get_latest_initial_anxiety_level_with_score_card():

    user = UserFactory.create()
    challenge = ChallengeFactory.create()
    AnxietyScoreCard.objects.create(
        challenge=challenge,
        anxiety_at_0_min='9',
        anxiety_at_120_min='2'
    )

    assert challenge.get_latest_initial_anxiety_level() == '9'

@pytest.mark.django_db
def test_get_latest_initial_anxiety_level_no_score_card():

    user = UserFactory.create()
    challenge = ChallengeFactory.create()

    assert challenge.get_latest_initial_anxiety_level() == -1
