from django.conf.urls import patterns, url
from hue import views

urlpatterns = patterns('',
  url(r'^group/(?P<group_id>.+)/(?P<action_id>.+)/$', views.takeAction, name="action")
)

