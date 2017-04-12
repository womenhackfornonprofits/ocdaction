import pytest

from tests.factories import UserFactory, TaskFactory
from tasks.models import Task

@pytest.mark.django_db
def test_create_task():

    user = UserFactory.create()

    # Check there are 0 tasks before a new task is added
    number_tasks = Task.objects.filter(user_id=user.id).count()
    assert number_tasks == 0

    task = TaskFactory.create()

    # Check there is 1 task after a new task is added
    number_tasks = Task.objects.filter(user_id=user.id).count()
    assert number_tasks == 1

@pytest.mark.django_db
def test_archive_task():

	user = UserFactory.create()
	task = TaskFactory.create()

	task.archive()
	assert task.is_archived == True
