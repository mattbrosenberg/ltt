from django.contrib import admin
from trancheur.models import Bond, Contract, MoneyMarket, Residual, Trade
from cashflow.models import Cashflow
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Investor


class AdminSite(AdminSite):
    site_title = 'FlexInvest Admin'
    index_title = 'Home'
    branding = "admin/logo.png"

admin_site = AdminSite()

def deactivate_account(modeladmin, request, queryset):
    queryset.update(is_active=False)
	deactivate_account.short_description = "Deactivate selected users"

def activate_account(modeladmin, request, queryset):
    queryset.update(is_active=True)
	activate_account.short_description = "Activate selected users"

class UserAdmin(UserAdmin):
    list_display = ('username', 'is_active', 'last_login', 'date_joined',)
    list_filter = ('groups', 'is_active',)
    date_hierarchy = 'date_joined'
    actions = [deactivate_account, activate_account]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Bond)
admin.site.register(Contract)
admin.site.register(MoneyMarket)
admin.site.register(Residual)
admin.site.register(Trade)
admin.site.register(Cashflow)

