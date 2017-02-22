__author__ = 'samuel'

from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url



urlpatterns=[
		url(r'^index/$', views.index, name='index'),
        url(r'^([0-9]+)/chapters$',views.get_chapters,name='course'),
        url(r'^([0-9]+)/sections$',views.get_section,name='sections'),
        url(r'^([0-9]+)/detail$',views.get_video_or_image,name='detail'),
        url(r'^([0-9]+)/watch$',views.watch,name='watch'),
    ]




