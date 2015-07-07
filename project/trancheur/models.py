from django.db import models
from django.contrib.auth.models import User

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
