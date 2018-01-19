from django import forms

from challenges.models import Challenge, AnxietyScoreCard


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('challenge_name', 'obsession', 'compulsion', 'exposure')
        widgets = {
            'obsession': forms.Textarea(attrs={'rows': '3'}),
            'compulsion': forms.Textarea(attrs={'rows': '3'}),
            'exposure': forms.Textarea(attrs={'rows': '3'})
        }

    def __init__(self, *args, **kwargs):
        super(ChallengeForm, self).__init__(*args, **kwargs)
        self.fields['challenge_name'].label = 'Your Fear'
        self.fields['obsession'].label = 'Your Obsession'
        self.fields['compulsion'].label = 'Your Compulsion'
        self.fields['exposure'].label = 'Your Exposure'

class AnxietyScoreCardForm(forms.ModelForm):

    class Meta:
        model = AnxietyScoreCard
        exclude = ['challenge']
        widgets = {
            'anxiety_at_0_min': forms.RadioSelect(attrs={'id': 'label'}),
            'anxiety_at_5_min': forms.RadioSelect(attrs={'id': 'label'}),
            'anxiety_at_10_min': forms.RadioSelect(attrs={'id': 'label'}),
            'anxiety_at_15_min': forms.RadioSelect(attrs={'id': 'label'}),
            'anxiety_at_30_min': forms.RadioSelect(attrs={'id': 'label'}),
            'anxiety_at_60_min': forms.RadioSelect(attrs={'id': 'label'}),
            'anxiety_at_120_min': forms.RadioSelect(attrs={'id': 'label'})
        }

    def __init__(self, *args, **kwargs):
        super(AnxietyScoreCardForm, self).__init__(*args, **kwargs)
        self.fields['anxiety_at_120_min'].required = False
