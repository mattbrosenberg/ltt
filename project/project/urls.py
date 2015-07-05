from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('main_controller.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clients/', include('users.urls')),
    url(r'^flex/', include('flex.urls')),
    url(r'^cashflow/', include('cashflow.urls')),
)
