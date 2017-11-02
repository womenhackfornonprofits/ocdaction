"""ocdaction URL Configuration
    main urls file, it imports all the app urls separately for tidiness.
"""
from django.conf.urls import url

from tasks.views import (
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
        r'^tasks/$',
        task_list,
        name="task-list"
    ),
    url(
        r'^tasks/(?P<archived>)archived/$',
        task_list,
        name="task-list-archived"
    ),
    url(
        r'^tasks/new/$',
        task_add,
        name="task-add"
    ),
    url(
        r'^tasks/(?P<task_id>\d+)/edit$',
        task_edit,
        name="task-edit"
    ),
    url(
        r'^tasks/(?P<task_id>\d+)/archive/$',
        task_archive,
        name="task-archive"
    ),
    url(
        r'^tasks/(?P<task_id>\d+)/$',
        task_score_form,
        name="task-score-form"
    ),
    url(
        r'^tasks/(?P<task_id>\d+)/complete/(?P<score_id>\d+)/$',
        task_complete,
        name="task-complete"
    ),
    url(
        r'^tasks/(?P<task_id>\d+)/summary/(?P<score_id>\d+)/$',
        task_summary,
        name="task-summary"
    ),
]
