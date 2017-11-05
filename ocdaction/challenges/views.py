from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from challenges.models import Challenge, AnxietyScoreCard
from challenges.forms import ChallengeForm, AnxietyScoreCardForm


@login_required
def challenge_list(request, archived=None):
    """
    Displays a list os user challenges on ACT view
    """
    template_name = "act/challenge_list.html"

    if archived == None:
        challenges = Challenge.objects.filter(user=request.user, is_archived=False).order_by('-created_at', '-updated_at')[:10]
        context = {'challenges': challenges}
    else:
        challenges = Challenge.objects.filter(user=request.user, is_archived=True).order_by('-created_at', '-updated_at')[:10]
        context = {'challenges': challenges, 'archived': True}

    return render(request, template_name, context)


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
        'act/challenge_add.html',
        {
            'challenge_form': challenge_form,
        }
    )


@login_required
def challenge_edit(request, challenge_id):
    """
    Edit a challenge
    """
    challenge_inst = get_object_or_404(Challenge, pk=challenge_id)

    if request.method == 'POST':
        challenge_form = ChallengeForm(request.POST, instance=challenge_inst)

        if challenge_form.is_valid():
            challenge = challenge_form.save(commit=False)
            challenge.user = request.user
            challenge.save()

            return redirect('challenge-list')
    else:
        challenge_form = ChallengeForm(instance=challenge_inst)

    context = {'challenge_form': challenge_form}

    return render(
         request,
         'act/challenge_edit.html',
         context
    )


@login_required
def challenge_archive(request, challenge_id):
    """
    Archive a challenge
    """
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    challenge.archive()

    return redirect('challenge-list')


@login_required
def challenge_complete(request, challenge_id, score_id):
    """
    Mark challenge completed
    """
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    anxiety_score_card = get_object_or_404(AnxietyScoreCard, pk=score_id)

    return render(
        request,
        'act/challenge_complete.html',
        {
            'challenge': challenge,
            'anxiety_score_card': anxiety_score_card,
        }
    )


@login_required
def challenge_summary(request, challenge_id, score_id):
    """
    Summary of a challenge
    """
    challenge = get_object_or_404(Task, pk=challenge_id)
    anxiety_score_card = get_object_or_404(AnxietyScoreCard, pk=score_id)

    return render(
        request,
        'act/challenge_summary.html',
        {
            'challenge': challenge,
            'anxiety_score_card': anxiety_score_card,
        }
    )


@login_required
def challenge_score_form(request, challenge_id):
    """
    Enter anxiety scores for the challenge
    """
    challenge = get_object_or_404(Task, pk=challenge_id)

    if request.method == "POST":
        anxiety_score_form = AnxietyScoreCardForm(request.POST)
        if anxiety_score_form.is_valid():
            anxiety_score_card = anxiety_score_form.save(commit=False)
            anxiety_score_card.challenge = challenge
            anxiety_score_card.save()

            return redirect('challenge-complete', challenge_id=challenge.id, score_id=anxiety_score_card.id)
    else:
        anxiety_score_form = AnxietyScoreCardForm()

    return render(
        request,
        'act/challenge_score_form.html',
        {
            'anxiety_score_form': anxiety_score_form,
            'challenge': challenge
        }
    )
