from django import forms

from tasks.models import Task, AnxietyScoreCard


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'task_fears', 'task_compulsions', 'task_goals')
        widgets = {
            'task_fears': forms.Textarea(attrs={'rows': '3'}),
            'task_compulsions': forms.Textarea(attrs={'rows': '3'}),
            'task_goals': forms.Textarea(attrs={'rows': '3'})
        }


class AnxietyScoreCardForm(forms.ModelForm):

    class Meta:
        model = AnxietyScoreCard
        exclude = ['task']

    def clean(self):
        cleaned_data = super(AnxietyScoreCardForm, self).clean()
        score_after_0_min = cleaned_data.get("score_after_0_min")
        score_after_5_min = cleaned_data.get("score_after_5_min")
        score_after_10_min = cleaned_data.get("score_after_10_min")
        score_after_15_min = cleaned_data.get("score_after_15_min")
        score_after_30_min = cleaned_data.get("score_after_30_min")
        score_after_60_min = cleaned_data.get("score_after_60_min")

        if any(x == '' for x in (
                score_after_0_min,
                score_after_5_min,
                score_after_10_min,
                score_after_15_min,
                score_after_30_min,
                score_after_60_min)):
            raise forms.ValidationError(
                "Please complete all of your anxiety levels"
            )
