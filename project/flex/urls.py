from django.conf.urls import patterns, include, url
from .views import Index, Investing, Portfolio, Account, Trades, All_deals

urlpatterns = patterns('',

    url(r'^$', Index.as_view()),
    url(r'^investing/', Investing.as_view()),
    url(r'^investing/all', All_deals.as_view()),
    url(r'^portfolio/', Portfolio.as_view()),
    url(r'^account/', Account.as_view()),
    url(r'^trades/', Trades.as_view()),

)
