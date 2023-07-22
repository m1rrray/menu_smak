from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'caption', 'price', 'category', 'weight', 'picture')
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
