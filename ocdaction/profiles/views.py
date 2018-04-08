from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from registration.backends.default import views as registration_views
from profiles.forms import OCDActionUserRegistrationForm
from django.contrib.auth.decorators import login_required


class RegistrationComplete(TemplateView):
    """
    The Registration Complete view.
    """

    template_name = "registration/registration_complete.html"


class ActivationComplete(TemplateView):
    """
    The Registration Complete view.
    """

    template_name = "registration/activation_complete.html"


class RegistrationView(registration_views.RegistrationView):
    """
    The Registration view.
    """

    template_name = 'registration/register.html'
    form_class = OCDActionUserRegistrationForm

@login_required
def my_account(request):
    return render(request, 'profiles/my_account.html')
