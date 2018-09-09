"""ocdaction URL Configuration
    main urls file, it imports all the app urls separately for tidiness.
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from core.views import home_index

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
        r'^learn/$',
        TemplateView.as_view(template_name='core/learn.html'),
        name="learn"
    ),
    url(
        r'^$',
        home_index,
        name="index"
    ),
    url(
        r'',
        include('profiles.urls')
    ),
    url(
        r'^challenges/',
        include('challenges.urls')
    ),
]
