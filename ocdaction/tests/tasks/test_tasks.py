import pytest

from tests.factories import UserFactory, TaskFactory
from tasks.models import Task


@pytest.mark.django_db
def test_create_task():

    user = UserFactory.create()

    # Check there are 0 challenges before a new challenge is added
    number_tasks = Task.objects.filter(user_id=user.id).count()
    assert number_tasks == 0

    task = TaskFactory.create()

    # Check there is 1 challenge after a new challenge is added
    # and that it's not archived
    number_tasks = Task.objects.filter(user_id=user.id).count()
    task = Task.objects.get(user_id=user.id)
    assert number_tasks == 1
    assert task.is_archived is False


@pytest.mark.django_db
def test_archive_task():

    user = UserFactory.create()
    task = TaskFactory.create()

    task.archive()
    assert task.is_archived is True
