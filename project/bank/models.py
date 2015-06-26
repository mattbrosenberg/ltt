from django.db import models

class Account(models.Model):
    user = models.ForeignKey('users.User', related_name='owner')
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
