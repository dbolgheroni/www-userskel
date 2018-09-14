from django.conf.urls import url, include
from .views import (IndexTemplateView,
		UserLoginView,)

urlpatterns = [
    url(r'^$', IndexTemplateView.as_view(),
            name='index'),
    url(r'^login/$', UserLoginView.as_view(),
            name='user-login'),
]


