# from django.db import models

# class Bond(models.Model):
#     cusip = models.CharField(max_length=9)
#     face = models.DecimalField(max_digits=15, decimal_places=2)
#     price = models.DecimalField(max_digits=15, decimal_places=3)
#     coupon = models.DecimalField(max_digits=15, decimal_places=5)
#     issuance_date = models.DateTimeField()
#     maturity = models.DateTimeField()
#     payments_per_year = models.IntegerField()

# class Contract(models.Model):
#     user = models.ForeignKey('users.User', related_name='user')
#     face = models.DecimalField(max_digits=15, decimal_places=2)
#     price = models.DecimalField(max_digits=15, decimal_places=3)
#     issuance_date = models.DateTimeField()
#     maturity = models.DateTimeField()

# class MoneyMarket(Contract):
#     coupon = models.DecimalField(max_digits=15, decimal_places=5)

# class InverseFloater(Contract):
#     payments_per_year = models.IntegerField()
    

