from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.hashers import make_password, check_password

class User(AbstractUser):
    type_of = models.CharField(max_length=50, blank=False)

    REQUIRED_FIELDS = ['email', 'type_of', 'is_active',]

    def __str__(self):
        return self.username

    @staticmethod
    def create_hash(password):
        return make_password(password)
 
    @staticmethod
    def check_hash(entered_password, hashed_password):
        if check_password(entered_password, hashed_password):
            return True
        else:
            return False


    # type_of = models.CharField(max_length=50, blank=False)
    # name = models.CharField(max_length=50, blank=False)
    # email = models.EmailField(unique=True, blank=False)
    # password = models.CharField(max_length=200, blank=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)