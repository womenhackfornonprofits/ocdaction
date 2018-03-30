from django.conf.urls import url

from .views import (
  my_account
)

urlpatterns = [
    url(
        r'^$',
        my_account,
        name="my-account"
    ),
]