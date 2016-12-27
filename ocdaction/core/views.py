from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomepageView(TemplateView):
    """
    The Homepage View.
    """
    template_name = "index.html"


class ContactView(TemplateView):
    """
    The Contact Us View.
    """
    template_name = "core/contact.html"


class AboutView(TemplateView):
    """
    The About Us View.
    """
    template_name = "core/about.html"


class MeetTheTeam(TemplateView):
    """
    Meet The Team View.
    """
    template_name = "core/team.html"


class TermsAndConditions(TemplateView):
    """
    Terms And Conditions View.
    """
    template_name = "core/terms_and_conditions.html"


class ThinkView(TemplateView):
    """
    The Think View.
    """
    template_name = "core/think.html"
