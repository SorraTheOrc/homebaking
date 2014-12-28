from django.conf.urls import patterns, include, url
from django.contrib import admin
from homebaking import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^connect/$', views.connect, name='connect'),
    url(r'^log/', include('log.urls')),
    url(r'^action/', include('log.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
