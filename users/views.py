from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import render


class LoginView(BaseLoginView):
    pass


class LogoutView(BaseLogoutView):
    pass