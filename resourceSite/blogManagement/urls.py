from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='blog'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.blog_detail, name='detail'),
]
