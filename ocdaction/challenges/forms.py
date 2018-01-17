from django import forms

from challenges.models import Challenge, AnxietyScoreCard


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('challenge_name', 'obsession', 'compulsion', 'exposure')
        widgets = {
            'challenge_name': forms.TextInput(attrs={'placeholder': 'This will appear in your Hierarchy'}),
            'obsession': forms.Textarea(attrs={'rows': '3', 'placeholder': 'What\'s the worry or thought that makes you anxious'}),
            'compulsion': forms.Textarea(attrs={'rows': '3', 'placeholder': 'What\'s the thing that you do to try to get rid of anxiety'}),
            'exposure': forms.Textarea(attrs={'rows': '3', 'placeholder': 'What is your homework set by your therapist'})
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ChallengeForm, self).__init__(*args, **kwargs)
        self.fields['challenge_name'].label = 'Your Fear'
        self.fields['obsession'].label = 'Your Obsession'
        self.fields['compulsion'].label = 'Your Compulsion'
        self.fields['exposure'].label = 'Your Exposure'


class AnxietyScoreCardForm(forms.ModelForm):

    class Meta:
        model = AnxietyScoreCard
        exclude = ['challenge']

    def __init__(self, *args, **kwargs):
        super(AnxietyScoreCardForm, self).__init__(*args, **kwargs)
        self.fields['anxiety_at_120_min'].required = False
