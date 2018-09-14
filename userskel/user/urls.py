from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login
from .views import (IndexTemplateView,
		UserLoginView, UserCreateView,)

urlpatterns = [
    url(r'^$', IndexTemplateView.as_view(),
            name='index'),
    url(r'^login/$', UserLoginView.as_view(),
            name='user-login'),
    url(r'^logout/$', logout_then_login,
            name='user-logout'),
    url(r'^signup/$', UserCreateView.as_view(),
            name='user-create'),
]


