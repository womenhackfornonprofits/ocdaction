from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from tasks.models import Task
from tasks.forms import TaskForm


@login_required
def task_list(request):
    """
    Displays a list os user tasks on ACT view
    """
    template_name = "dashboard/act/task_list.html"
    tasks = Task.objects.filter(user=request.user, is_archived=False).order_by('-created_at', '-updated_at')[:10]

    return render(request, template_name, {'tasks': tasks})


@login_required
def task_add(request):
    """
    Add a new task
    """
    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('task-list')
    else:
        task_form = TaskForm()

    return render(
        request,
        'dashboard/act/task_add.html',
        {
            'task_form': task_form,
        }
    )


@login_required
def task_edit(request, task_id):
    """
    Edit a task
    """
    task_inst = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task_inst)

        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('task-list')
    else:
        task_form = TaskForm(instance=task_inst)

    context = {'task_form': task_form}

    return render(
         request,
         'dashboard/act/task_edit.html',
         context
    )

@login_required
def task_archive(request, task_id):
    """
    Archive a task
    """
    task = get_object_or_404(Task, pk=task_id)
    task.archive()
    return redirect('task-list')

