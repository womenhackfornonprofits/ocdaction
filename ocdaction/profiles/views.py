from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from registration.backends.default import views as registration_views
from profiles.forms import OCDActionUserRegistrationForm


# Create your views here.
class LoginView(TemplateView):
    """
    The Login view.
    """

    template_name = "profiles/login.html"

class RegistrationComplete(TemplateView):
    """
    The Registration Complete view.
    """

    template_name = "registration/registration_complete.html"


class RegistrationView(registration_views.RegistrationView):
    """
    The Registration view.
    """

    template_name = 'profiles/register.html'
    form_class = OCDActionUserRegistrationForm
    success_url = '/accounts/registration-complete/'