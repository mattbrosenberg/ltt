from django.conf.urls import include, url, patterns
from django.contrib import admin
from users.views import IndexView, LoginView, RegisterView, Update, LogoutView

urlpatterns = patterns('users.views',
    url(r'^$', IndexView.as_view()),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^update/$', Update.as_view(), name='update'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
)
