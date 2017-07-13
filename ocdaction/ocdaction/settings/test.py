from ocdaction.settings import *

import django

SECRET_KEY = 'FAKEforTEST'

INSTALLED_APPS = INSTALLED_APPS + [
    'tests',
]


class DisableMigrations(object):

    def __init__(self):
        self._django_version = django.VERSION

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        if self._django_version >= (1, 9):
            return None
        else:
            return 'notmigrations'


MIGRATION_MODULES = DisableMigrations()
