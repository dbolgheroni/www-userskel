from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, UsernameField,
        PasswordChangeForm, SetPasswordForm)
from django.utils.translation import ugettext, ugettext_lazy as _

class NoHelpUserCreationForm(UserCreationForm):
    username = UsernameField()
    email = forms.fields.EmailField()
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = get_user_model()
        #fields = ("username", "email",)
        fields = UserCreationForm.Meta.fields + ('email',)
        field_classes = {"username": UsernameField}


#class ProfileForm(forms.ModelForm):
#    class Meta:
#        model = get_user_model()
#        fields = ['username', 'email', 'first_name', 'last_name']


# delete help
class UserPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
    )


# delete help
class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
    )
