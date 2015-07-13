from django.conf.urls import include, url, patterns
from django.contrib import admin
from users.views import Login, Register, Update, Logout

urlpatterns = patterns('users.views',
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^update/$', Update.as_view(), name='update'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
)
