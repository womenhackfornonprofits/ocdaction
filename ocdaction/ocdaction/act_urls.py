"""ocdaction URL Configuration
    main urls file, it imports all the app urls separately for tidiness.
"""
from django.conf.urls import url

from core.views import (
    task_list,
    task_add,
)

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
]
