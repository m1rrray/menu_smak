from django.contrib import admin
from .models import NewUser


# Register your models here.
class UsersPanel(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'fullname', 'phone')
    empty_value_display = "-пусто-"


admin.site.register(NewUser, UsersPanel)
