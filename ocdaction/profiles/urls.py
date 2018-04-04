"""
    ocdaction URL Configuration
    profile/user specific urls for auth workflows
"""
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from .views import RegistrationView, RegistrationComplete, ActivationComplete, my_account
from .forms import OCDActionUserRegistrationForm


urlpatterns = [
    url(
        r'^register/$',
        RegistrationView.as_view(form_class=OCDActionUserRegistrationForm),
        name='register',
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
        auth_views.LoginView.as_view(template_name='profiles/login.html'),
        name='login',
    ),
    url(
        r'^logout/$',
        auth_views.LogoutView.as_view(template_name='profiles/logout.html'),
        name='logout',
    ),
    url(
        r'^password-reset/$',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
        name='password_reset',
    ),
    url(
        r'^password-reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done',
    ),
    url(
        r'^password-reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete',
    ),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(
    r'^my-account',
        my_account,
        name="my-account"
    ),
]
