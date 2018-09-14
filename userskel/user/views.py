from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import (LoginView, PasswordResetView,)
from django.contrib import messages
from .forms import NoHelpUserCreationForm


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'index.html'


# Login
class UserLoginView(LoginView):
    template_name = "users/login.html"
    template_name = "user/login.html"


# Create
class UserCreateView(CreateView):
    template_name = "user/create.html"
    form_class = NoHelpUserCreationForm
    success_url = reverse_lazy("user-login")

    def form_valid(self, form):
        messages.success(self.request, "Signed up successfully. "
                "Log in now.")
        return super(UserCreateView, self).form_valid(form)


# Password Reset
class UserPasswordResetView(PasswordResetView):
    template_name = "user/password_reset.html"
    success_url = reverse_lazy("password-reset")

    def form_valid(self, form):
        messages.info(self.request, "A password reset link was created. "
                "Please check your email and confirm.")
        return super(UserPasswordResetView, self).form_valid(form)
