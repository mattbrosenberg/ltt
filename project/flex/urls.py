from django.conf.urls import patterns, include, url
from .views import Index, Investing, Portfolio, Account, Trades, AllAvailableTranches

urlpatterns = patterns('',

    url(r'^$', Index.as_view()),
    url(r'^investing/$', Investing.as_view()),
    url(r'^portfolio/$', Portfolio.as_view()),
    url(r'^account/$', Account.as_view()),
    url(r'^trades/$', Trades.as_view()),
    url(r'^api/investing/all_available_tranches/$', AllAvailableTranches.as_view()),

)
