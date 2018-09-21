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
            name='login'),
    url(r'^logout/$', logout_then_login,
            name='logout'),
    url(r'^signup/$', UserCreateView.as_view(),
            name='user_create'),
    url(r'^password_reset/$', UserPasswordResetView.as_view(),
            name='password_reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', UserPasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    url(r'^password_reset_complete/$', UserPasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
    url(r'^password_change/$', UserPasswordChangeView.as_view(),
            name='password_change'),
    url(r'^password_change_done/$', UserPasswordChangeDoneView.as_view(),
            name='password_change_done'),
    url(r'^profile/$', UserDetailView.as_view(),
            name='user_detail'),
]
