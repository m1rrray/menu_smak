from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from posts.models import Post
from users.usermanager import UserManager


class Address(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_addresses')
    street = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=15)

    def __str__(self):
        if self.apartment_number:
            return f"{self.street}, кв {self.apartment_number}"
        else:
            return f"{self.street}"


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_orders')
    order_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    items = models.ManyToManyField("OrderItem", blank=True, related_name='order_items')

    def __str__(self):
        return f"Order #{self.pk} by {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_items')
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.pk} - {self.product.title} ({self.quantity} pcs)"


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField( max_length=30, blank=True)
    phone = models.CharField(max_length=50, unique=True)
    addresses = models.ManyToManyField(Address, blank=True, related_name='user_addresses')
    orders = models.ManyToManyField(Order, blank=True, related_name='user_orders')
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name






