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