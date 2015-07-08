from django.db import models
from django.contrib.auth.models import User
import datetime

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
        return Bond.objects.filter(auction_date__gte=datetime.datetime.today())

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
            if residual.trades.all() != []:
                funded_residuals.append(residual)
        return funded_residuals

    def num_funded_residuals(self):
        return len(self.get_all_funded_residuals())

    def num_available_residuals(self):
        return self.num_residuals - num_funded_residuals

    def percent_residuals_funded(self):
        return ( self.num_funded_residuals() // self.num_residuals() ) * 100

    def days_to_auction(self):
        timedelta = self.auction_date - datetime.datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)
        return  timedelta.days

class Contract(models.Model):
    face = models.DecimalField(max_digits=15, decimal_places=2)
    issuance_date = models.DateField()
    maturity = models.DateField()
    bond = models.ForeignKey('Bond', related_name='contracts')

class Trade(models.Model):
    buyer = models.ForeignKey(User, related_name='purchases')
    seller = models.ForeignKey(User, related_name='sales')
    contract = models.ForeignKey('Contract', related_name='trades')
    price = models.DecimalField(max_digits=6, decimal_places=5)
    time = models.DateTimeField()

    class Meta:
        get_latest_by = "time"

class MoneyMarket(Contract):
    coupon = models.DecimalField(max_digits=15, decimal_places=5)

class Residual(Contract):
    payments_per_year = models.IntegerField()

class BondPrice(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=5)
    date = models.DateField()
    bond = models.ForeignKey('Bond', related_name='prices')

    class Meta:
        get_latest_by = "date"
