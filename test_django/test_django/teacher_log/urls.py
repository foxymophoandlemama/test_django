'''
Created on Sep 2, 2013

@author: davide
'''
import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'scholars/$', views.ListScholarsView.as_view(), name='scholars'),
    url(r'scholars/(?P<pk>\d+)/$', views.ScholarDetailView.as_view(), name='scholar')
)