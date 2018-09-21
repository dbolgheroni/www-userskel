from django.urls import reverse_lazy
from django.views.generic import (TemplateView, CreateView, DetailView,
        UpdateView,)
from django.contrib.auth.views import (LoginView, PasswordResetView,
        PasswordChangeView, PasswordChangeDoneView,
        PasswordResetConfirmView, PasswordResetCompleteView,)
from django.contrib import messages
from .forms import (NoHelpUserCreationForm, UserPasswordChangeForm,
        UserSetPasswordForm,)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'index.html'


# Login
class UserLoginView(LoginView):
    template_name = "user/login.html"


# Create
class UserCreateView(CreateView):
    template_name = "user/create.html"
    form_class = NoHelpUserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Signed up successfully. "
                "Log in now.")
        return super(UserCreateView, self).form_valid(form)


# Password Reset
class UserPasswordResetView(PasswordResetView):
    template_name = "user/password_reset.html"
    success_url = reverse_lazy("password_reset")
    email_template_name = "user/password_reset_email.html"

    def form_valid(self, form):
        messages.info(self.request, "A password reset link was created. "
                "Please check your email and confirm.")
        return super(UserPasswordResetView, self).form_valid(form)


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "user/password_reset_confirm.html"
    post_reset_login = True
    form_class = UserSetPasswordForm


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "user/password_reset_complete.html"


# Password Change
class UserPasswordChangeView(PasswordChangeView):
    template_name = "user/password_change.html"
    form_class = UserPasswordChangeForm


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "user/password_change_done.html"


# Profile
class UserDetailView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form = UserChangeForm
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy("user_detail")
    template_name = "user/profile.html"

    def get_object(self):
        obj = get_object_or_404(get_user_model(), username=self.request.user)
        return obj

    def form_valid(self, form):
        messages.success(self.request, "Profile saved.")
        return super(UserDetailView, self).form_valid(form)
