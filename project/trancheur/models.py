from django.db import models

class Bond(models.Model):
    cusip = models.CharField(max_length=9)
    face = models.DecimalField(max_digits=15, decimal_places=2)
    coupon = models.DecimalField(max_digits=15, decimal_places=5)
    issuance_date = models.DateField()
    maturity = models.DateField()
    payments_per_year = models.IntegerField()

    def __str__(self):
        return self.cusip

class Contract(models.Model):
    face = models.DecimalField(max_digits=15, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=3)
    issuance_date = models.DateField()
    maturity = models.DateField()
    bond = models.ForeignKey('Bond', related_name='contracts')
    trades = models.ManyToManyField('users.User', through='Trade', through_fields=('contract', 'buyer'))


class Trade(models.Model):
    buyer = models.ForeignKey('users.User', related_name='purchases')
    seller = models.ForeignKey('users.User', related_name='sales')
    contract = models.ForeignKey('Contract')
    price = models.DecimalField(max_digits=15, decimal_places=3)
    time = models.DateTimeField()


class MoneyMarket(Contract):
    coupon = models.DecimalField(max_digits=15, decimal_places=5)

class Residual(Contract):
    payments_per_year = models.IntegerField()
    
class BondPrice(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=5)
    date = models.DateField()
    bond = models.ForeignKey('Bond', related_name='prices')

