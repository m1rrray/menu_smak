from django.contrib import admin
from .models import User


class UsersPanel(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'phone')
    empty_value_display = "-пусто-"


admin.site.register(User, UsersPanel)
