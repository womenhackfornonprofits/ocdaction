from django import forms

from profiles.models import OCDActionUser
from registration.forms import RegistrationForm


class OCDActionUserRegistrationForm(RegistrationForm):

    yes_no_choices = (
        (1, 'Yes'),
        (0, 'No'),
    )

    have_ocd = forms.ChoiceField(choices=yes_no_choices, label='Do you have an OCD diagnosis?')
    date_birth = forms.DateField(widget=forms.SelectDateWidget(), label='Date of birth')

    class Meta:
        model = OCDActionUser
        fields = ('email', 'password1', 'password2', 'username')
