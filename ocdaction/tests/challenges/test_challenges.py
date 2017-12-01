import pytest

from tests.factories import UserFactory, ChallengeFactory
from challenges.models import Challenge, AnxietyScoreCard
from django.test import TestCase, RequestFactory
from challenges.views import *
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_create_challenge():

    user = UserFactory.create()

    # Check there are 0 challenges before a new challenge is added
    number_challenges = Challenge.objects.filter(user_id=user.id).count()
    assert number_challenges == 0

    challenge = ChallengeFactory.create()
    challenge.user = user
    challenge.save()

    # Check there is 1 challenge after a new challenge is added
    # and that it's not archived or in progress
    number_challenges = Challenge.objects.filter(user_id=user.id).count()
    challenge = Challenge.objects.get(user_id=user.id)
    assert number_challenges == 1
    assert challenge.is_archived is False
    assert challenge.in_progress is False


@pytest.mark.django_db
def test_archive_challenge():

    challenge = ChallengeFactory.create()

    # Check that the is_archived flag is set to true when the archive function is called
    challenge.archive()
    assert challenge.is_archived is True

@pytest.mark.django_db
def test_save_challenge():

    challenge = ChallengeFactory.create()

    # Check that on saving a challenge in_progress is set to False by default
    challenge.save()
    assert challenge.in_progress is False

@pytest.mark.django_db
def test_get_latest_initial_anxiety_level_with_score_card():

    challenge = ChallengeFactory.create()
    AnxietyScoreCard.objects.create(
        challenge=challenge,
        anxiety_at_0_min='9',
        anxiety_at_120_min='2'
    )
    AnxietyScoreCard.objects.create(
        challenge=challenge,
        anxiety_at_0_min='6',
        anxiety_at_120_min='1'
    )

    # Check that when getting the initial anxiety level, the most recent is returned
    assert challenge.get_latest_initial_anxiety_level() == '6'

@pytest.mark.django_db
def test_get_latest_initial_anxiety_level_no_score_card():

    challenge = ChallengeFactory.create()

    # Check that if there is no anxiety score card for a challenge, -1 is returned
    assert challenge.get_latest_initial_anxiety_level() == -1

class ChallengesInProgressTest(TestCase):

    def setUp(self):

        self.user = UserFactory.create()
        self.challenge = ChallengeFactory.create()
        self.challenge1 = ChallengeFactory.create()

    def test_mark_challenge_in_progress(self):

        challenge = self.challenge
        challenge.in_progress = True
        challenge.save()
        assert challenge.in_progress is True

    def test_mark_challenge_in_progress_when_another_user_in_progress(self):

        challenge = self.challenge
        challenge1 = self.challenge1
        challenge.in_progress = True
        challenge1.in_progress = True
        challenge.save()
        challenge1.save()

        # Check that more than one user can have a challenge in progress
        assert challenge.in_progress is True
        assert challenge1.in_progress is True

    def test_mark_challenge_in_progress_when_another_in_progress(self):

        challenge = self.challenge
        challenge1 = self.challenge1
        challenge1.user = challenge.user

        challenge.in_progress = True
        challenge.save()

        challenge1.in_progress = True
        challenge1.save()

        challenge.refresh_from_db()
        challenge1.refresh_from_db()

        # Check that challenge is now not in progress because challenge1 was marked as in_progress
        assert challenge.in_progress is False
        assert challenge1.in_progress is True


class ViewsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory.create()

    def test_challenge_list_view(self):
        request = self.factory.get(reverse('challenge-list'))
        request.user = self.user
        response = challenge_list(request)
        self.assertEqual(response.status_code, 200)

    def test_challenge_archive_view(self):
        request = self.factory.get(reverse('challenge-list-archived'))
        request.user = self.user
        response = challenge_list_archived(request)
        self.assertEqual(response.status_code, 200)
