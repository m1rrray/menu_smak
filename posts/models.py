from django.db import models

# Create your models here.


class Post(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=150)
    price = models.IntegerField()
    category = models.CharField(max_length=30)
    weight = models.IntegerField()