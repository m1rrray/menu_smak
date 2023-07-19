from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    user = models.ForeignKey('NewUser', on_delete=models.CASCADE, related_name='user_addresses')
    street = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=15)

    def __str__(self):
        if self.apartment_number:
            return f"{self.street}, кв {self.apartment_number}"
        else:
            return f"{self.street}"


class NewUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    addresses = models.ManyToManyField(Address, blank=True, related_name='user_addresses')




