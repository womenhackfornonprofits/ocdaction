from django.views.generic import TemplateView

from registration.backends.default import views as registration_views
from profiles.forms import OCDActionUserRegistrationForm


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
