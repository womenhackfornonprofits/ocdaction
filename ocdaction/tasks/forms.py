from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'task_fears', 'task_compulsions', 'task_goals')
        widgets = {
            'task_fears': forms.Textarea(attrs={'rows': '3'}),
            'task_compulsions': forms.Textarea(attrs={'rows': '3'}),
            'task_goals': forms.Textarea(attrs={'rows': '3'})
        }
