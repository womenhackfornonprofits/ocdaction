"""ocdaction URL Configuration
    Tasks specific urls for tasks workflows
"""
from django.conf.urls import url

from .views import (
    challenge_list,
    challenge_add,
    challenge_edit,
    challenge_archive,
    challenge_score_form,
    challenge_complete,
    challenge_summary
)

urlpatterns = [
    url(
        r'^$',
        challenge_list,
        name="challenge-list"
    ),
    url(
        r'^(?P<archived>)archived/$',
        challenge_list,
        name="challenge-list-archived"
    ),
    url(
        r'^new/$',
        challenge_add,
        name="challenge-add"
    ),
    url(
        r'^(?P<challenge_id>\d+)/edit$',
        challenge_edit,
        name="challenge-edit"
    ),
    url(
        r'^(?P<challenge_id>\d+)/archive/$',
        challenge_archive,
        name="challenge-archive"
    ),
    url(
        r'^(?P<challenge_id>\d+)/$',
        challenge_score_form,
        name="challenge-score-form"
    ),
    url(
        r'^(?P<challenge_id>\d+)/complete/(?P<score_id>\d+)/$',
        challenge_complete,
        name="challenge-complete"
    ),
    url(
        r'^(?P<challenge_id>\d+)/summary/(?P<score_id>\d+)/$',
        challenge_summary,
        name="challenge-summary"
    ),
]
