import factory.django

from profiles.models import OCDActionUser
from tasks.models import Task
import datetime


# Factories
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OCDActionUser
        django_get_or_create = (
            'username',
            'date_birth',
            'have_ocd'
        )

    username = 'testuser'
    date_birth = datetime.date(2000, 1, 2)
    have_ocd = True


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task
        django_get_or_create = (
            'task_name',
            'is_archived',
            'task_fears',
            'task_compulsions',
            'task_goals'
        )

    task_name = 'taskname'
    is_archived = False
    task_fears = 'fears'
    task_compulsions = 'compulsions'
    task_goals = 'goals'
    user = factory.SubFactory(UserFactory)

