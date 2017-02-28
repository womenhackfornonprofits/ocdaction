# from django.test import TestCase


# Create your tests here.
def add(x, y):
    return x + y


def test_add():
    assert add(1, 1) == 2
