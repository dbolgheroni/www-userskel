from django.conf.urls import url, include
from .views import IndexTemplateView

urlpatterns = [
    url(r'^$', IndexTemplateView.as_view(),
            name='index'),
]


