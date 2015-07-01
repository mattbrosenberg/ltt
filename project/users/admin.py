from django.contrib import admin
from users.models import User
from trancheur.models import Bond, MoneyMarket, InverseFloater

# Register your models here.

admin.site.register(User)
admin.site.register(Bond)
admin.site.register(MoneyMarket)
admin.site.register(InverseFloater)
