"""ocdaction URL Configuration
    main urls file, it imports all the app urls separately for tidiness.
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    url(
        r'^admin/',
        admin.site.urls
    ),
    url(
        r'^contact/$',
        TemplateView.as_view(template_name='core/contact.html'),
        name="contact"
    ),
    url(
        r'^meet-the-team/$',
        TemplateView.as_view(template_name='core/team.html'),
        name="team"
    ),
    url(
        r'^think/$',
        TemplateView.as_view(template_name='core/think.html'),
        name="think"
    ),
    url(
        r'^terms-and-conditions/$',
        TemplateView.as_view(template_name='core/terms_and_conditions.html'),
        name="terms_and_conditions"
    ),
    url(
        r'^$',
        TemplateView.as_view(template_name='index.html'),
        name="index"
    ),
    url(
        r'^users/',
        include('profiles.urls')
    ),
    url(
        r'^act/',
        include('ocdaction.tasks_urls')
    ),
]
