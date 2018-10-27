from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ctOS, name='ctOS'),
     url(r'^info/$', views.info, name='info'),
     url(r'^info_full/$', views.info_full, name='info_full'),
     url(r'^command/$', views.command, name='command'),
     url(r'^command_full/$', views.command_full, name='command_full'),
     url(r'^chat/$', views.chat, name='chat'),
     url(r'^hacked/$', views.hacked, name='hacked'),
     url(r'^admini/$', views.admini, name='admini'),


     url(r'^id1338/$', views.id1338, name='id1338'),
     url(r'^id9395/$', views.id9395, name='id9395'),
]
