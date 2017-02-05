"""
    ocdaction URL Configuration
    profile/user specific urls for auth workflows
"""
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from .views import RegistrationView, RegistrationComplete, ActivationComplete
from .forms import OCDActionUserRegistrationForm


urlpatterns = [
    url(
        r'^register/$',
        RegistrationView.as_view(form_class=OCDActionUserRegistrationForm), name='register',
    ),
    url(
        r'^register/complete/$',
        RegistrationComplete.as_view(), name='registration_complete',
    ),
    url(
        r'^register/activation-complete',
        ActivationComplete.as_view(), name='activation_complete',
    ),
    url(
        r'^login/$',
        auth_views.login,
        {'template_name': 'profiles/login.html'},
        name='login',
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'template_name': 'profiles/logout.html'},
        name='logout',
    ),
    url(
        r'^password-reset/$',
        auth_views.password_reset,
        {'template_name': 'profiles/password_reset.html'},
        name='password_reset',
    ),
    url(
        r'^password-reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'profiles/password_reset_done.html'},
        name='password_reset_done',
    ),
    url(
        r'^reset/(?P<uidb64>[\w\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        auth_views.password_reset_confirm,
        {'template_name': 'profiles/password_reset_confirm.html'},
        name='password_reset_confirm',
    ),
    url(
        r'^password-reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'profiles/password_reset_complete.html'},
        name='password_reset_complete',
    ),
    url(r'^accounts/', include('registration.backends.default.urls')),

]
