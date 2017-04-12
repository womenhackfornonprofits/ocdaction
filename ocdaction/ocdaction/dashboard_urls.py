"""ocdaction URL Configuration
    main urls file, it imports all the app urls separately for tidiness.
"""
from django.conf.urls import url

from tasks.views import (
    task_list,
    task_add,
    task_edit
)

from core.views import dashboard_index

urlpatterns = [
    url(
        r'^tasks/$',
        task_list,
        name="task-list"
    ),
    url(
        r'^tasks/new/$',
        task_add,
        name="task-add"
    ),
    url(
        r'^tasks/(?P<task_id>\d+)/$',
        task_edit,
        name="task-edit"
    ),
    url(
        r'^index/$',
        dashboard_index,
        name="dashboard-index"
    ),
]
