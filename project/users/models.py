from django.db import models
from django.contrib.auth.models import User
from trancheur.models import Trade

class Investor(models.Model):
    user = models.OneToOneField(User, related_name='investor')

    def __str__(self):
        return self.user.username

    def get_currently_owned_contracts(self):
        purchases = self.purchases.all()
        contracts = []
        for purchase in purchases:
            if purchase.contract.trades.latest('date') == purchase:
                contracts.append(purchase.contract)
        return contracts

class Analyst(models.Model):
    user = models.OneToOneField(User, related_name='analyst')

