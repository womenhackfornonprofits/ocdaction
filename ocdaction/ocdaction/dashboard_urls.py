"""ocdaction URL Configuration
    main urls file, it imports all the app urls separately for tidiness.
"""
from django.conf.urls import url

from tasks.views import (
    task_list,
    task_add,
    task_edit,
    task_archive
)

from core.views import dashboard_index

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
        r'^index/$',
        dashboard_index,
        name="dashboard-index"
    ),
]
