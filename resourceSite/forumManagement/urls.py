from django.conf.urls import url
from . import views




urlpatterns=[
	url(r'^index/$', views.get_index, name='index'),
    url(r'^([0-9]+)/$',views.get_node_topics,name='node_topic'),
    url(r'^create/$', views.get_create, name='topic_create'),
    url(r'^post/$', views.post_create, name='topic_post'),
    url(r'^(?P<topic_id>\d+)/detail/$', views.post_view, name='view_topic'),
]
