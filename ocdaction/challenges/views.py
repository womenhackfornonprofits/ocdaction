from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from tasks.models import Task, AnxietyScoreCard
from tasks.forms import TaskForm, AnxietyScoreCardForm


@login_required
def task_list(request, archived=None):
    """
    Displays a list os user challenges on ACT view
    """
    template_name = "act/task_list.html"

    if archived == None:
        tasks = Task.objects.filter(user=request.user, is_archived=False).order_by('-created_at', '-updated_at')[:10]
        context = {'challenges': tasks}
    else:
        tasks = Task.objects.filter(user=request.user, is_archived=True).order_by('-created_at', '-updated_at')[:10]
        context = {'challenges': tasks, 'archived': True}

    return render(request, template_name, context)


@login_required
def task_add(request):
    """
    Add a new challenge
    """
    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('challenge-list')
    else:
        task_form = TaskForm()

    return render(
        request,
        'act/task_add.html',
        {
            'task_form': task_form,
        }
    )


@login_required
def task_edit(request, task_id):
    """
    Edit a challenge
    """
    task_inst = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task_inst)

        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('challenge-list')
    else:
        task_form = TaskForm(instance=task_inst)

    context = {'task_form': task_form}

    return render(
         request,
         'act/task_edit.html',
         context
    )


@login_required
def task_archive(request, task_id):
    """
    Archive a challenge
    """
    task = get_object_or_404(Task, pk=task_id)
    task.archive()

    return redirect('challenge-list')


@login_required
def task_complete(request, task_id, score_id):
    """
    Mark challenge completed
    """
    task = get_object_or_404(Task, pk=task_id)
    anxiety_score_card = get_object_or_404(AnxietyScoreCard, pk=score_id)

    return render(
        request,
        'act/task_complete.html',
        {
            'challenge': task,
            'anxiety_score_card': anxiety_score_card,
        }
    )


@login_required
def task_summary(request, task_id, score_id):
    """
    Summary of a challenge
    """
    task = get_object_or_404(Task, pk=task_id)
    anxiety_score_card = get_object_or_404(AnxietyScoreCard, pk=score_id)

    return render(
        request,
        'act/task_summary.html',
        {
            'challenge': task,
            'anxiety_score_card': anxiety_score_card,
        }
    )


@login_required
def task_score_form(request, task_id):
    """
    Enter anxiety scores for the challenge
    """
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        anxiety_score_form = AnxietyScoreCardForm(request.POST)
        if anxiety_score_form.is_valid():
            anxiety_score_card = anxiety_score_form.save(commit=False)
            anxiety_score_card.task = task
            anxiety_score_card.save()

            return redirect('challenge-complete', task_id=task.id, score_id=anxiety_score_card.id)
    else:
        anxiety_score_form = AnxietyScoreCardForm()

    return render(
        request,
        'act/task_score_form.html',
        {
            'anxiety_score_form': anxiety_score_form,
            'challenge': task
        }
    )
