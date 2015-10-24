from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.SubView.as_view(), name='sub'),
    url(r'^(?P<sub_id>[0-9]+)/post/(?P<post_id>[0-9]+)/$', views.post_view, name='post'),
    url(r'^(?P<sub_id>[0-9]+)/post/(?P<post_id>[0-9]+)/comment/$', views.top_level_comment, name='comment'),
]
