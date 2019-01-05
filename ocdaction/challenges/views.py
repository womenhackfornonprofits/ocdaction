import csv
import json

from collections import OrderedDict

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from challenges.models import Challenge, AnxietyScoreCard
from challenges.forms import ChallengeForm, AnxietyScoreCardForm

from profiles.models import OCDActionUser

def get_data_for_challenge_chart(challenge, num_challenges):
    """
    :param challenge:
    :return: all chart data for a challenge
    """

    global latest_scores
    global latest_anxiety_score_card_label
    global latest_anxiety_score_card_data
    global data_sets

    anxiety_score_cards_for_challenge = challenge.anxietyscorecard_set.values_list('anxiety_at_0_min',
                                                                                   'anxiety_at_5_min',
                                                                                   'anxiety_at_10_min',
                                                                                   'anxiety_at_15_min',
                                                                                   'anxiety_at_30_min',
                                                                                   'anxiety_at_60_min',
                                                                                   'anxiety_at_120_min',
                                                                                   'updated_at').order_by('-updated_at')[:num_challenges]

    first = True
    data_sets = OrderedDict()
    for anxietyscorecard in anxiety_score_cards_for_challenge:
        if first:
            # return the data for the most recent score card
            first = False
            latest_anxietyscorecard_as_list = list(anxietyscorecard)
            latest_anxiety_score_card_date = latest_anxietyscorecard_as_list.pop()
            latest_scores = []
            for i in latest_anxietyscorecard_as_list:
                try:
                    i = int(i)
                except:
                    i = None
                latest_scores.append(i)
            latest_anxiety_score_card_data = json.dumps(latest_scores)
            latest_anxiety_score_card_label = latest_anxiety_score_card_date.strftime("%d %b")
        else:
            # return the data for the remaining score cards
            anxietyscorecard_as_list = list(anxietyscorecard)
            anxiety_score_card_date = anxietyscorecard_as_list.pop()
            scores = []
            for i in anxietyscorecard_as_list:
                try:
                    i = int(i)
                except:
                    i = None
                scores.append(i)
            data_sets[anxiety_score_card_date.strftime("%d %b %H:%M")] = json.dumps(scores)


@login_required
def challenge_list(request):
    """
    Displays a list of user challenges on Challenge view
    """
    challenges = Challenge.objects.filter(user=request.user, is_archived=False).order_by(
        '-in_progress',
        '-created_at',
        '-updated_at'
    )[:10]

    sorted_challenges_by_anxiety = sorted(challenges.all(), reverse=True, key = lambda c: int(c.get_latest_initial_anxiety_level()))
    sorted_challenges = sorted(sorted_challenges_by_anxiety, reverse=True, key = lambda c: c.in_progress)

    challenge_in_progress = Challenge.objects.filter(user=request.user, in_progress=True)
    anxiety_score_card = AnxietyScoreCard.objects.filter(challenge=challenge_in_progress).last()

    context = {
        'challenges': challenges,
        'sorted_challenges': sorted_challenges,
        'another_challenge_in_progress': challenge_in_progress,
        'anxiety_score_card': anxiety_score_card
    }

    return render(request, 'challenge/challenge_list.html', context)


@login_required
def challenge_list_archived(request):
    """
    Displays a list of user archived challenges
    """
    challenges_archived = Challenge.objects.filter(
        user=request.user,
        is_archived=True
    ).order_by(
        '-created_at',
        '-updated_at'
    )[:10]
    context = {'challenges_archived': challenges_archived}

    return render(request, 'challenge/challenge_list_archived.html', context)


@login_required
def challenge_add(request):
    """
    Add a new challenge
    """
    if request.method == 'POST':
        challenge_form = ChallengeForm(request.POST)

        if challenge_form.is_valid():
            challenge = challenge_form.save(commit=False)
            challenge.user = request.user
            challenge.save()

            return redirect('challenge-list')
    else:
        challenge_form = ChallengeForm()

    return render(
        request,
        'challenge/challenge_add.html',
        {
            'challenge_form': challenge_form,
        }
    )


@login_required
def challenge_view(request, challenge_uuid):
    """
    View a challenge
    """
    challenge = get_object_or_404(Challenge.objects.filter(user=request.user), uuid=challenge_uuid)
    anxiety_score_cards = AnxietyScoreCard.objects.filter(challenge=challenge).order_by('-id')[:3]

    get_data_for_challenge_chart(challenge, 5)

    context = {
        'challenge': challenge,
        'anxiety_score_cards': anxiety_score_cards,
        'latest_scores': latest_scores,
        'latest_anxiety_score_card_data': latest_anxiety_score_card_data,
        'latest_anxiety_score_card_label': latest_anxiety_score_card_label,
        'data_sets': data_sets
    }

    return render(request, 'challenge/challenge_view.html', context)


@login_required
def challenge_edit(request, challenge_uuid):
    """
    Edit a challenge
    """
    challenge_inst = get_object_or_404(Challenge.objects.filter(user=request.user), uuid=challenge_uuid)

    if request.method == 'POST':
        challenge_form = ChallengeForm(request.POST, instance=challenge_inst)

        if challenge_form.is_valid():
            challenge = challenge_form.save(commit=False)
            challenge.user = request.user
            challenge.save()

            context = {'challenge': challenge_inst}
            return render(request, 'challenge/challenge_view.html', context)

    else:
        challenge_form = ChallengeForm(instance=challenge_inst)

    context = {'challenge_form': challenge_form, 'challenge': challenge_inst}

    return render(
       request,
       'challenge/challenge_edit.html',
       context
    )


@login_required
def challenge_archive(request, challenge_uuid):
    """
    Archive a challenge
    """
    challenge = get_object_or_404(Challenge.objects.filter(user=request.user), uuid=challenge_uuid)
    challenge.archive()

    return redirect('challenge-list')


@login_required
def challenge_summary(request, challenge_uuid):
    """
    Mark challenge complete and display summary of a challenge
    """
    challenge = get_object_or_404(Challenge.objects.filter(user=request.user), uuid=challenge_uuid)
    anxiety_score_cards = AnxietyScoreCard.objects.filter(challenge=challenge).order_by('-id')[:3]

    challenge.in_progress = False
    challenge.save()

    context = {'challenge': challenge, 'anxiety_score_cards': anxiety_score_cards}

    return render(
        request,
        'challenge/challenge_summary.html',
        context
    )


@login_required
def challenge_score_form_new(request, challenge_uuid):
    """
    Start doing a challenge, creating a new score card
    """

    challenge = get_object_or_404(Challenge.objects.filter(user=request.user), uuid=challenge_uuid)

    if request.method == "POST":
        anxiety_score_form = AnxietyScoreCardForm(request.POST)
        if anxiety_score_form.is_valid():
            anxiety_score_card = anxiety_score_form.save(commit=False)
            anxiety_score_card.challenge = challenge
            challenge.in_progress = True
            challenge.save()
            anxiety_score_card.save()

            return redirect(
                challenge_score_form,
                challenge_uuid=challenge_uuid,
                score_uuid=anxiety_score_card.uuid
            )

    else:
        anxiety_score_form = AnxietyScoreCardForm()

    return render(
        request,
        'challenge/challenge_score_form.html',
        {
            'anxiety_score_form': anxiety_score_form,
            'challenge': challenge
        }
    )


@login_required
def challenge_score_form(request, challenge_uuid, score_uuid):
    """
    Continue doing a challenge, on an existing score card
    """

    challenge = get_object_or_404(Challenge.objects.filter(user=request.user), uuid=challenge_uuid)
    anxiety_score_card = get_object_or_404(AnxietyScoreCard, uuid=score_uuid)

    if request.method == "POST":
        anxiety_score_form = AnxietyScoreCardForm(request.POST, instance=anxiety_score_card)
        if anxiety_score_form.is_valid():
            anxiety_score_card = anxiety_score_form.save(commit=False)
            anxiety_score_card.challenge = challenge
            anxiety_score_card.save()
            challenge.save()

    else:
        anxiety_score_form = AnxietyScoreCardForm(instance=anxiety_score_card)

    context = {
        'anxiety_score_form': anxiety_score_form,
        'challenge': challenge,
        'anxiety_score_card': anxiety_score_card
    }

    return render(
        request,
        'challenge/challenge_score_form.html',
        context
    )


@login_required
def challenge_results(request, challenge_uuid):
    """
    See the results for today's challenges
    """
    challenge = get_object_or_404(Challenge.objects.filter(user=request.user), uuid=challenge_uuid)

    get_data_for_challenge_chart(challenge, 5)

    context = {
        'challenge': challenge,
        'latest_scores': latest_scores,
        'latest_anxiety_score_card_data': latest_anxiety_score_card_data,
        'latest_anxiety_score_card_label': latest_anxiety_score_card_label,
        'data_sets': data_sets
    }

    return render(
        request,
        'challenge/challenge_results.html',
        context
    )


@login_required
def challenge_erase_my_record(request):
    return render(request, 'challenge/challenge_erase_my_record.html')


def delete_challenges(user):

    challenges = Challenge.objects.filter(user=user)

    for challenge in challenges:
        challenge.delete()


@login_required
def delete_users_challenges(request):
    """
    Delete all challenges and associated score cards for a user
    """
    delete_challenges(request.user)

    return render(request, 'profiles/my_account_confirm.html', {'deleted_user': False})


@login_required
def export_challenges_for_user(request):
    """
    Export a user's challenge data to csv.
    The score cards for each challenge are returned, with the most recent first.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="challenges.csv"'

    writer = csv.writer(response)
    writer.writerow(['Email address', 'Nickname', 'Date of birth', 'Has OCD diagnosis?'])

    user = OCDActionUser.objects.get(id=request.user.id)
    writer.writerow([user.email, user.nickname, user.date_birth, user.have_ocd, ])
    writer.writerow('')

    writer.writerow(['Challenge name',
                     'Archived?',
                     'In progress?',
                     'Obsession',
                     'Compulsion',
                     'Exposure',
                     'Created',
                     'Last updated'])

    challenges = Challenge.objects.filter(user=request.user)

    for challenge in challenges:
        challenge_attrs = (challenge.challenge_name,
                           challenge.is_archived,
                           challenge.in_progress,
                           challenge.obsession,
                           challenge.compulsion,
                           challenge.exposure,
                           challenge.created_at.strftime('%d-%m-%Y %H:%M'),
                           challenge.updated_at.strftime('%d-%m-%Y %H:%M'))

        anxietyscorecard_attrs_list = challenge.anxietyscorecard_set.values_list('anxiety_at_0_min',
                                                                         'anxiety_at_5_min',
                                                                         'anxiety_at_10_min',
                                                                         'anxiety_at_15_min',
                                                                         'anxiety_at_30_min',
                                                                         'anxiety_at_60_min',
                                                                         'anxiety_at_120_min').order_by('-id')

        writer.writerow(challenge_attrs)

        if anxietyscorecard_attrs_list:
            writer.writerow(['Anxiety at 0 min',
                             'Anxiety at 5 min',
                             'Anxiety at 10 min',
                             'Anxiety at 15 min',
                             'Anxiety at 30 min',
                             'Anxiety at 60 min',
                             'Anxiety at 120 min'])
        else:
            writer.writerow('')

        for anxietyscorecard in anxietyscorecard_attrs_list:
            writer.writerow(anxietyscorecard)

        writer.writerow('')

    return response





