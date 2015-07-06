from django.db import models

class Bond(models.Model):
<<<<<<< HEAD
    cusip = models.CharField(max_length=9, unique = True)
=======
    cusip = models.CharField(max_length=9, unique=True)
>>>>>>> 0c9cc642e8e159d67dc49140d1ee2f3753c2e4dc
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
    buyer = models.ForeignKey('users.Investor', related_name='purchases')
    seller = models.ForeignKey('users.Investor', related_name='sales')
    contract = models.ForeignKey('Contract', related_name='trades')
    price = models.DecimalField(max_digits=6, decimal_places=5)
    time = models.DateTimeField()

class MoneyMarket(Contract):
    coupon = models.DecimalField(max_digits=15, decimal_places=5)

class Residual(Contract):
    payments_per_year = models.IntegerField()

class BondPrice(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=5)
    date = models.DateField()
    bond = models.ForeignKey('Bond', related_name='prices')
