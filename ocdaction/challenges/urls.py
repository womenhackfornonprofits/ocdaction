"""ocdaction URL Configuration
    Challenges specific urls for challenges workflows
"""
from django.conf.urls import url

from .views import *

urlpatterns = [
    url(
        r'^$',
        challenge_list,
        name="challenge-list"
    ),
    url(
        r'^archived/$',
        challenge_list_archived,
        name="challenge-list-archived"
    ),
    url(
        r'^new/$',
        challenge_add,
        name="challenge-add"
    ),
    url(
        r'^(?P<challenge_id>\d+)/$',
        challenge_view,
        name="challenge"
    ),
    url(
        r'^(?P<challenge_id>\d+)/edit/$',
        challenge_edit,
        name="challenge-edit"
    ),
    url(
        r'^(?P<challenge_id>\d+)/archive/$',
        challenge_archive,
        name="challenge-archive"
    ),
    url(
        r'^(?P<challenge_id>\d+)/exposure/$',
        challenge_score_form_new,
        name="challenge-score-form-new"
    ),
    url(
        r'^(?P<challenge_id>\d+)/exposure/(?P<score_id>\d+)/$',
        challenge_score_form,
        name="challenge-score-form"
    ),
    url(
        r'^(?P<challenge_id>\d+)/summary/(?P<score_id>\d+)/$',
        challenge_summary,
        name="challenge-summary"
    ),
    url(
        r'^erase-my-record/$',
        challenge_erase_my_record,
        name="challenge-erase-my-record"
    ),
    url(
        r'^delete-users-challenges/$',
        delete_users_challenges,
        name="delete-users-challenges"
    ),
]
