from django.db import models

class Libor(models.Model):
    date = models.DateField(unique=True)
    rate = models.DecimalField(max_digits=8, decimal_places=5)
