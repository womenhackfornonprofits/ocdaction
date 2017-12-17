import pytest

from tests.factories import UserFactory, ChallengeFactory
from challenges.models import Challenge, AnxietyScoreCard
from django.test import TestCase, RequestFactory
from challenges.views import *
from challenges.forms import *
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


# Tests for marking challenges in progress
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


# Test each of the views
class ViewsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory.create()
        self.challenge = ChallengeFactory.create()
        self.score_card = AnxietyScoreCard.objects.create(
            challenge=self.challenge,
            anxiety_at_0_min='9',
            anxiety_at_120_min='2'
        )

    def test_challenge_list(self):
        request = self.factory.get(reverse('challenge-list'))
        request.user = self.user
        response = challenge_list(request)
        assert response.status_code == 200

    def test_challenge_list_archived(self):
        request = self.factory.get(reverse('challenge-list-archived'))
        request.user = self.user
        response = challenge_list_archived(request)
        assert response.status_code == 200

    def test_challenge_add(self):
        request = self.factory.get(reverse('challenge-add'))
        request.user = self.user
        response = challenge_add(request)
        assert response.status_code == 200

    def test_challenge_view(self):
        request = self.factory.get(reverse('challenge', args=(self.challenge.pk,)))
        request.user = self.user
        response = challenge_view(request, self.challenge.pk)
        assert response.status_code == 200

    def test_challenge_edit(self):
        request = self.factory.get(reverse('challenge-edit', args=(self.challenge.pk,)))
        request.user = self.user
        response = challenge_edit(request, self.challenge.pk)
        assert response.status_code == 200

    def test_challenge_archive(self):
        request = self.factory.get(reverse('challenge-archive', args=(self.challenge.pk,)))
        request.user = self.user
        response = challenge_archive(request, self.challenge.pk)
        assert response.status_code == 302

    def test_challenge_summary(self):
        request = self.factory.get(reverse('challenge-summary', args=(self.challenge.pk, self.score_card.pk,)))
        request.user = self.user
        response = challenge_summary(request, self.challenge.pk, self.score_card.pk)
        assert response.status_code == 200

    def test_challenge_score_form_new(self):
        request = self.factory.get(reverse('challenge-score-form-new', args=(self.challenge.pk,)))
        request.user = self.user
        response = challenge_score_form_new(request, self.challenge.pk)
        assert response.status_code == 200

    def test_challenge_score_form(self):
        request = self.factory.get(reverse('challenge-score-form', args=(self.challenge.pk, self.score_card.pk,)))
        request.user = self.user
        response = challenge_score_form(request, self.challenge.pk, self.score_card.pk)
        assert response.status_code == 200


# Test the forms
@pytest.mark.parametrize(
    'challenge_name, obsession, compulsion, exposure, validity',
    [('', '', '', '', False),
     ('', 'o', 'c', 'e', False),
     ('challenge', '', '', '', True),
     ('challenge', 'o', 'c', 'e', True),
     ])

def test_challenge_form(challenge_name, obsession, compulsion, exposure, validity):
    form = ChallengeForm(data={
        'challenge_name': challenge_name,
        'obsession': obsession,
        'compulsion': compulsion,
        'exposure': exposure,
    })

    assert form.is_valid() is validity

@pytest.mark.parametrize(
    'anxiety_at_0_min, anxiety_at_5_min, anxiety_at_10_min, anxiety_at_15_min, anxiety_at_30_min, anxiety_at_60_min, '
    'anxiety_at_120_min, validity',
    [('', '', '', '', '', '', '', False),
     ('', '1', '', '', '', '', '', False),
     ('', '', '1', '', '', '', '', False),
     ('', '', '', '1', '', '', '', False),
     ('', '', '', '', '1', '', '', False),
     ('', '', '', '', '', '1', '', False),
     ('', '', '', '', '', '', '1', False),
     ('1', '', '', '', '', '', '', True),
     ('1', '', '', '', '', '', '1', True),
     ])

def test_anxietyscore_form(anxiety_at_0_min, anxiety_at_5_min, anxiety_at_10_min, anxiety_at_15_min, anxiety_at_30_min,
                           anxiety_at_60_min, anxiety_at_120_min, validity):
    form = AnxietyScoreCardForm(data={
        'anxiety_at_0_min': anxiety_at_0_min,
        'anxiety_at_5_min': anxiety_at_5_min,
        'anxiety_at_10_min': anxiety_at_10_min,
        'anxiety_at_15_min': anxiety_at_15_min,
        'anxiety_at_30_min': anxiety_at_30_min,
        'anxiety_at_60_min': anxiety_at_60_min,
        'anxiety_at_120_min': anxiety_at_120_min,
    })

    assert form.is_valid() is validity
