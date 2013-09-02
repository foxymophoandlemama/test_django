from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^teacher_log/', include('teacher_log.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)