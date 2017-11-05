"""ocdaction URL Configuration
    Tasks specific urls for tasks workflows
"""
from django.conf.urls import url

from .views import (
    task_list,
    task_add,
    task_edit,
    task_archive,
    task_score_form,
    task_complete,
    task_summary
)

urlpatterns = [
    url(
        r'^$',
        task_list,
        name="challenge-list"
    ),
    url(
        r'^(?P<archived>)archived/$',
        task_list,
        name="challenge-list-archived"
    ),
    url(
        r'^new/$',
        task_add,
        name="challenge-add"
    ),
    url(
        r'^(?P<task_id>\d+)/edit$',
        task_edit,
        name="challenge-edit"
    ),
    url(
        r'^(?P<task_id>\d+)/archive/$',
        task_archive,
        name="challenge-archive"
    ),
    url(
        r'^(?P<task_id>\d+)/$',
        task_score_form,
        name="challenge-score-form"
    ),
    url(
        r'^(?P<task_id>\d+)/complete/(?P<score_id>\d+)/$',
        task_complete,
        name="challenge-complete"
    ),
    url(
        r'^(?P<task_id>\d+)/summary/(?P<score_id>\d+)/$',
        task_summary,
        name="challenge-summary"
    ),
]
