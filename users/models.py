from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

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


# class NewUser(AbstractUser):
#     username = models.CharField(max_length=100, unique=True)
#     fullname = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     addresses = models.ManyToManyField(Address, blank=True, related_name='user_addresses')


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField( max_length=30, blank=True)
    phone = models.CharField(max_length=50, unique=True)
    addresses = models.ManyToManyField(Address, blank=True, related_name='user_addresses')
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



