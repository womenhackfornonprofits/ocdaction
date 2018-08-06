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
        r'^(?P<challenge_uuid>[0-9a-f-]+)/$',
        challenge_view,
        name="challenge"
    ),
    url(
        r'^(?P<challenge_uuid>[0-9a-f-]+)/edit/$',
        challenge_edit,
        name="challenge-edit"
    ),
    url(
        r'^(?P<challenge_uuid>[0-9a-f-]+)/archive/$',
        challenge_archive,
        name="challenge-archive"
    ),
    url(
        r'^(?P<challenge_uuid>[0-9a-f-]+)/exposure/$',
        challenge_score_form_new,
        name="challenge-score-form-new"
    ),
    url(
        r'^(?P<challenge_uuid>[0-9a-f-]+)/exposure/(?P<score_uuid>[0-9a-f-]+)/$',
        challenge_score_form,
        name="challenge-score-form"
    ),
    url(
        r'^(?P<challenge_uuid>[0-9a-f-]+)/summary/(?P<score_uuid>[0-9a-f-]+)/$',
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
    url(
        r'^export-challenges-for-user/$',
        export_challenges_for_user,
        name="export-challenges-for-user"
    ),
]
