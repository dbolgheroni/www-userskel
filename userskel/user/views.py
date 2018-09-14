from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import (LoginView,)

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'index.html'


# Login
class UserLoginView(LoginView):
    template_name = "users/login.html"
