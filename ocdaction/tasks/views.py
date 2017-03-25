from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tasks.models import Task
from tasks.forms import TaskForm, EditTaskForm


@login_required
def task_list(request):
    """
    Displays a list os user tasks on ACT view
    """
    template_name = "dashboard/act/task_list.html"
    tasks = Task.objects.filter(user=request.user, is_archived=False)

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
def task_edit(request):
    """
    Edit a task
    """
    task = Task.objects.get(id=1)
    if request.method == 'POST':
        edit_task_form = EditTaskForm(request.POST, instance=task)

        if edit_task_form.is_valid():
            task = edit_task_form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('task-list')
    else:
        edit_task_form = EditTaskForm(instance=task)

    context = {'edit_task_form': edit_task_form}

    return render(
        request,
        'dashboard/act/task_edit.html',
        {
            'edit_task_form': edit_task_form,
        }
    )