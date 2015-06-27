from django.conf.urls import patterns, include, url
from .views import Index, Auctions, Portfolio, Account

urlpatterns = patterns('',

    url(r'^$', Index.as_view()),
    url(r'^auctions/', Auctions.as_view()),
    url(r'^portfolio/', Portfolio.as_view()),
    url(r'^account/', Account.as_view()),

)
