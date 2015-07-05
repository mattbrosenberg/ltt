from django.contrib import admin
from users.models import User
from trancheur.models import Bond, Contract, MoneyMarket, Residual, Trade
from cashflow.models import Cashflow

# Register your models here.

admin.site.register(User)
admin.site.register(Bond)
admin.site.register(Contract)
admin.site.register(MoneyMarket)
admin.site.register(Residual)
admin.site.register(Trade)
admin.site.register(Cashflow)
