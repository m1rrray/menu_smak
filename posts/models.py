from django.db import models

from cart.models import Promotions


# Create your models here.


class Post(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=150)
    price = models.IntegerField()
    category = models.CharField(max_length=30)
    weight = models.IntegerField()

    def to_dict(self):
        """
        Преобразует объект модели Post в словарь.
        """
        return {
            'picture': self.picture.url if self.picture else '',
            'title': self.title,
            'caption': self.caption,
            'price': self.price,
            'category': self.category,
            'weight': self.weight,
        }