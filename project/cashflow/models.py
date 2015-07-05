from django.db import models

class Cashflow(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    contract = models.ForeignKey('trancheur.Contract', related_name='cashflows')
