from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login
from .views import (IndexTemplateView,
        UserLoginView, UserCreateView, UserPasswordResetView,
        UserDetailView, UserPasswordChangeView, UserPasswordChangeDoneView,
        UserPasswordResetConfirmView, UserPasswordResetCompleteView)

urlpatterns = [
    url(r'^$', IndexTemplateView.as_view(),
            name='index'),
    url(r'^login/$', UserLoginView.as_view(),
            name='user-login'),
    url(r'^logout/$', logout_then_login,
            name='user-logout'),
    url(r'^signup/$', UserCreateView.as_view(),
            name='user-create'),
    url(r'^password_reset/$', UserPasswordResetView.as_view(),
            name='password-reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', UserPasswordResetConfirmView.as_view(),
            name='password-reset-confirm'),
    url(r'^password_reset_complete/$', UserPasswordResetCompleteView.as_view(),
            name='password-reset-complete'),
    url(r'^password_change/$', UserPasswordChangeView.as_view(),
            name='password-change'),
    url(r'^password_change_done/$', UserPasswordChangeDoneView.as_view(),
            name='password-change-done'),
    url(r'^profile/$', UserDetailView.as_view(),
            name='user-detail'),
]
