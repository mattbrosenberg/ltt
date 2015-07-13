from django.db import models
from django.contrib.auth.models import User

class User(User):
    class Meta:
        proxy = True

    def get_all_money_spent(self):
        amount_spent = 0
        for trade in self.purchases.all():
            amount_spent += (float(trade.price) * float(trade.contract.face))
        return round(amount_spent, 2)