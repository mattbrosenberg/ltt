from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from users.views import IndexView, LoginView, RegisterView, WelcomeView, LogoutView

urlpatterns = patterns('users.views',
    url(r'^$', IndexView.as_view()),
    url(r'^login/$', csrf_exempt(LoginView.as_view()), name='login'),
    url(r'^register/$', csrf_exempt(RegisterView.as_view()), name='register'),
    url(r'^welcome/$', WelcomeView.as_view(), name='welcome'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
)
