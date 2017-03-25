from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_name', 'task_fears', 'task_compulsions', 'task_goals')

class EditTaskForm(forms.ModelForm):

    class Meta:
    	model = Task
    	fields = ('task_name','task_fears', 'task_compulsions', 'task_goals')