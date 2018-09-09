from django import forms

from challenges.models import Challenge, AnxietyScoreCard


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('challenge_name', 'obsession', 'compulsion', 'exposure')
        widgets = {
            'challenge_name': forms.TextInput(),
            'obsession': forms.Textarea(attrs={'rows': '3'}),
            'compulsion': forms.Textarea(attrs={'rows': '3'}),
            'exposure': forms.Textarea(attrs={'rows': '3'})
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ChallengeForm, self).__init__(*args, **kwargs)
        self.fields['challenge_name'].label = 'Your Fear'
        self.fields['challenge_name'].help_text = 'This will be the name of your challenge and will appear in your hierarchy list.'
        self.fields['obsession'].label = 'Your Obsession'
        self.fields['obsession'].help_text = 'What\'s the worry or thought that makes you anxious?'
        self.fields['compulsion'].label = 'Your Compulsion'
        self.fields['compulsion'].help_text = 'What\'s the thing that you do to try to get rid of anxiety?'
        self.fields['exposure'].label = 'Your Exposure'
        self.fields['exposure'].help_text = 'What is your homework set by your therapist?'

class AnxietyScoreCardForm(forms.ModelForm):

    class Meta:
        model = AnxietyScoreCard
        exclude = ['challenge']
        widgets = {
            'anxiety_at_0_min': forms.RadioSelect(),
            'anxiety_at_5_min': forms.RadioSelect(),
            'anxiety_at_10_min': forms.RadioSelect(),
            'anxiety_at_15_min': forms.RadioSelect(),
            'anxiety_at_30_min': forms.RadioSelect(),
            'anxiety_at_60_min': forms.RadioSelect(),
            'anxiety_at_120_min': forms.RadioSelect()
        }

    def __init__(self, *args, **kwargs):
        super(AnxietyScoreCardForm, self).__init__(*args, **kwargs)
        self.fields['anxiety_at_120_min'].required = False
