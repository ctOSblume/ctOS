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


     url(r'^id6957/$', views.id6957, name='id6957'), #+
     url(r'^id9750/$', views.id9750, name='id9750'), #+
     url(r'^id0085/$', views.id0085, name='id0085'), #+-
     url(r'^id0024/$', views.id0024, name='id0024'), #+-

     url(r'^id2303/$', views.id2303, name='id2303'), #+
     url(r'^id9395/$', views.id9395, name='id9395'), #+

     url(r'^id5572/$', views.id5572, name='id5572'), #+
     url(r'^id3998/$', views.id3998, name='id3998'), #+
     url(r'^id1338/$', views.id1338, name='id1338'), #+-

     url(r'^id7557/$', views.id7557, name='id7557'), #+-

     url(r'^id4575/$', views.id4575, name='id4575'), #+-
     url(r'^id7540/$', views.id7540, name='id7540'), #-
     url(r'^id7939/$', views.id7939, name='id7939'), #-
     url(r'^id5886/$', views.id5886, name='id5886'), #-

     url(r'^id1124/$', views.id1124, name='id1124'), #?
     url(r'^id5452/$', views.id5452, name='id5452'), #?
     url(r'^id8794/$', views.id8794, name='id8794'), #?

     url(r'^id0787/$', views.id0787, name='id0787'), #+-

]
