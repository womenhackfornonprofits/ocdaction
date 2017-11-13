from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from challenges.models import Challenge, AnxietyScoreCard
from challenges.forms import ChallengeForm, AnxietyScoreCardForm


@login_required
def challenge_list(request):
    """
    Displays a list of user challenges on Challenge view
    """
    challenges = Challenge.objects.filter(user=request.user, is_archived=False).order_by('-in_progress', '-created_at', '-updated_at')[:10]
    challenge_in_progress = Challenge.objects.filter(in_progress=True)
    anxiety_score_card = AnxietyScoreCard.objects.filter(challenge=challenge_in_progress).last()

    context = {'challenges': challenges, 'another_challenge_in_progress': challenge_in_progress, 'anxiety_score_card': anxiety_score_card}

    return render(request, 'challenge/challenge_list.html', context)


@login_required
def challenge_list_archived(request):
    """
    Displays a list of user archived challenges
    """
    challenges = Challenge.objects.filter(user=request.user, is_archived=True).order_by('-created_at', '-updated_at')[:10]
    context = {'challenges': challenges}

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
def challenge_view(request, challenge_id):
    """
    View a challenge
    """
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    context = {'challenge': challenge}

    return render(request, 'challenge/challenge_view.html', context)


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

            context = {'challenge': challenge_inst}
            return render(request, 'challenge/challenge_view.html', context)

    else:
        challenge_form = ChallengeForm(instance=challenge_inst)

    context = {'challenge_form': challenge_form}

    return render(
         request,
         'challenge/challenge_edit.html',
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

    challenge.in_progress = False
    challenge.save()

    return render(
        request,
        'challenge/challenge_complete.html',
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
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    anxiety_score_card = get_object_or_404(AnxietyScoreCard, pk=score_id)

    return render(
        request,
        'challenge/challenge_summary.html',
        {
            'challenge': challenge,
            'anxiety_score_card': anxiety_score_card,
        }
    )


@login_required
def challenge_score_form_new(request, challenge_id):
    """
    Start doing a challenge, creating a new score card
    """

    challenge = get_object_or_404(Challenge, pk=challenge_id)

    if request.method == "POST":
        anxiety_score_form = AnxietyScoreCardForm(request.POST)
        if anxiety_score_form.is_valid():
            anxiety_score_card = anxiety_score_form.save(commit=False)
            anxiety_score_card.challenge = challenge
            challenge.in_progress = True
            challenge.save()
            anxiety_score_card.save()

            return redirect(challenge_score_form, challenge_id=challenge_id, score_id=anxiety_score_card.id)

    else:
        anxiety_score_form = AnxietyScoreCardForm()

    return render(request, 'challenge/challenge_score_form.html', {'anxiety_score_form': anxiety_score_form, 'challenge': challenge})

@login_required
def challenge_score_form(request, challenge_id, score_id):
    """
    Continue doing a challenge, on an existing score card
    """

    challenge = get_object_or_404(Challenge, pk=challenge_id)
    anxiety_score_card = get_object_or_404(AnxietyScoreCard, pk=score_id)

    if request.method == "POST":
        anxiety_score_form = AnxietyScoreCardForm(request.POST, instance=anxiety_score_card)
        if anxiety_score_form.is_valid():
            anxiety_score_card = anxiety_score_form.save(commit=False)
            anxiety_score_card.challenge = challenge
            anxiety_score_card.save()

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

