from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Investor
from trancheur.models import Bond, MoneyMarket, Residual, Contract, Trade
from cashflow.models import Cashflow

class InvestorInline(admin.StackedInline):
    model = Investor
    can_delete = False
    verbose_name_plural = 'investor'

class UserAdmin(UserAdmin):
    inlines = (InvestorInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Bond)
admin.site.register(Contract)
admin.site.register(MoneyMarket)
admin.site.register(Residual)
admin.site.register(Trade)
admin.site.register(Cashflow)
