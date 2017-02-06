"""ocdaction URL Configuration
    main urls file, it imports all the app urls separately for tidiness.
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from core.views import (
    HomepageView,
    ContactView,
    AboutView,
    MeetTheTeam,
    TermsAndConditions,
    ThinkView,
    ActView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view(), name="index"),
    url(r'^contact', ContactView.as_view(), name="contact"),
    url(r'^about', AboutView.as_view(), name="about"),
    url(r'^act', ActView, name="act"),
    url(r'^meet-the-team', MeetTheTeam.as_view(), name="team"),
    url(r'^think', ThinkView.as_view(), name="think"),
    url(r'^terms-and-conditions', TermsAndConditions.as_view(), name="terms_and_conditions"),
    url(r'^users/', include('profiles.urls')),
    url(r'^dashboard/$', TemplateView.as_view(
        template_name='dashboard/dashboard_index.html'
    )),
]
