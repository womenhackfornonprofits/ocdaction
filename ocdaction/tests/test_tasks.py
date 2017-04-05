import pytest
import datetime
import factory
from pytest_factoryboy import register

from profiles.models import OCDActionUser
from tasks.models import Task

@pytest.mark.django_db
def test_addtask():
    testuser = OCDActionUser(username='autouser',
                         date_birth=datetime.date(2000, 1, 2),
                         have_ocd=True,
                         email='autouser@yopmail.com'
                         )
    testuser.save()

    # Check there are 0 tasks before a new task is added
    number_tasks = Task.objects.filter(user_id=testuser.id).count()
    assert number_tasks == 0

    task = Task(task_name='taskname',
                is_archived=False,
                task_fears='fears',
                task_compulsions='compulsions',
                task_goals='goals',
                user_id=testuser.id
                )

    task.save()

    # Check there is 1 task after a new task is added
    number_tasks = Task.objects.filter(user_id=testuser.id).count()
    assert number_tasks == 1

    # Teardown
    OCDActionUser.objects.get(username='autouser').delete()


# class UserFactory(factory.Factory):
#
#     class Meta:
#         model = OCDActionUser
#
# register(UserFactory)
#
# @pytest.mark.django_db
# def test_addtaskUsefactory(user_factory):
#     testuser = user_factory(username='autouser',
#                          date_birth=datetime.date(2000, 1, 2),
#                          have_ocd=True,
#                          email='autouser@yopmail.com'
#                             )