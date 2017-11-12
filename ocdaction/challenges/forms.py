from django import forms

from challenges.models import Challenge, AnxietyScoreCard


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('challenge_name', 'challenge_fears', 'challenge_compulsions', 'challenge_goals')
        widgets = {
            'challenge_fears': forms.Textarea(attrs={'rows': '3'}),
            'challenge_compulsions': forms.Textarea(attrs={'rows': '3'}),
            'challenge_goals': forms.Textarea(attrs={'rows': '3'})
        }


class AnxietyScoreCardForm(forms.ModelForm):

    class Meta:
        model = AnxietyScoreCard
        exclude = ['challenge']

    def __init__(self, *args, **kwargs):
        super(AnxietyScoreCardForm, self).__init__(*args, **kwargs)
        self.fields['anxiety_at_120_min'].required = False
