from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<user_id>\d+)/info/$', views.user_info, name='userInfo'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.user_login,name='signin'),
    url(r'^logout/$', views.user_logout, name='signout'),
    url(r'^setting/$', views.setting, name='info_setting'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.reset_confirm, name='password_reset_confirm'),
    url(r'^reset/$', views.reset, name='password_reset'),
]

