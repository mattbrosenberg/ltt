from django.db import models
from django.contrib.auth.models import User
from cashflow.models import Cashflow
import datetime
from django.utils import timezone

class Bond(models.Model):
    cusip = models.CharField(max_length=9, unique = True)
    face = models.DecimalField(max_digits=15, decimal_places=2)
    coupon = models.DecimalField(max_digits=15, decimal_places=5)
    initial_price = models.DecimalField(max_digits=6, decimal_places=5)
    dated_date = models.DateField()
    auction_date = models.DateTimeField()
    maturity = models.DateField()
    payments_per_year = models.IntegerField()

    def __str__(self):
        return self.cusip

    @classmethod
    def get_all_unauctioned_bonds(cls):
        return Bond.objects.filter(auction_date__gt=timezone.now())

    def get_all_residuals(self):
        residuals = []
        for contract in self.contracts.all():
            if hasattr(contract, 'residual'):
                residuals.append(contract)
        return residuals

    def num_residuals(self):
        return len(self.get_all_residuals())

    def get_all_funded_residuals(self):
        funded_residuals = []
        for residual in self.get_all_residuals():
            if residual.trades.all().count() > 0:
                funded_residuals.append(residual)
        return funded_residuals

    def num_funded_residuals(self):
        return len(self.get_all_funded_residuals())

    def num_available_residuals(self):
        return self.num_residuals() - self.num_funded_residuals()

    def percent_residuals_funded(self):
        percent_funded = self.num_funded_residuals() / self.num_residuals() * 100
        return round(percent_funded, 1)

    def days_to_auction(self):
        timedelta = self.auction_date - timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
        return  timedelta.days

class Contract(models.Model):
    face = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    bond = models.ForeignKey('Bond', related_name='contracts')

    class Meta:
        get_latest_by = "created_at"

    def owner(self):
        try:
            return self.trades.latest().buyer.username
        except:
            return None

    def __str__(self):
        return self.bond.cusip + " | " + str(self.face) + " | " + str(self.owner())


class Trade(models.Model):
    buyer = models.ForeignKey(User, related_name='purchases')
    seller = models.ForeignKey(User, related_name='sales')
    contract = models.ForeignKey('Contract', related_name='trades')
    price = models.DecimalField(max_digits=6, decimal_places=5)
    time = models.DateTimeField()

    class Meta:
        get_latest_by = "time"

    def __str__(self):
        if hasattr(self.contract, "residual"):
            type_of = "Residual"
        else:
            type_of = "MoneyMarket"
        return self.contract.bond.cusip + " | " + str(self.price) + " | " + type_of

class MoneyMarket(Contract):
    coupon = models.DecimalField(max_digits=15, decimal_places=5)
    issuance_date = models.DateField()
    maturity = models.DateField()

class Residual(Contract):
    payments_per_year = models.IntegerField()

class BondPrice(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=5)
    date = models.DateField()
    bond = models.ForeignKey('Bond', related_name='prices')

    class Meta:
        get_latest_by = "date"
