import pytest

from tests.factories import UserFactory
from profiles.models import OCDActionUser
from django.test import TestCase, RequestFactory
from profiles.views import *
from profiles.forms import *
from django.core.urlresolvers import reverse

@pytest.mark.django_db
def test_create_user():

    # Check there are 0 users before a new user is added
    number_users = OCDActionUser.objects.count()
    assert number_users == 0

    # Check there is 1 user after a new user is added
    UserFactory.create()
    number_users = OCDActionUser.objects.count()
    assert number_users == 1
