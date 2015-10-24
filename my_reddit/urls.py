from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<sub_id>[0-9]+)/$', views.sub_view, name='sub'),
]
