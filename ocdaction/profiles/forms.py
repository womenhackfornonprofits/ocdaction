from django import forms

from profiles.models import OCDActionUser
from registration.forms import RegistrationForm

class OCDActionUserRegistrationForm(RegistrationForm):
	
	class Meta:
		model = OCDActionUser
		fields = ('email','password1', 'password2', 'username')


        