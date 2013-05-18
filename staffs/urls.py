from django.conf.urls import patterns, url

from staffs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
