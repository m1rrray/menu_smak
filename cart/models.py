from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Promotions(models.Model):
    promocode = models.CharField(max_length=100, default=None)
    discount = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
