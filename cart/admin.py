from django.contrib import admin

from cart.models import Promotions


class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['promocode', 'discount']  # Отображаемые поля в списке
    search_fields = ['promocode']  # Поля, по которым можно выполнять поиск


# Зарегистрируйте модель Promotions и класс PromotionsAdmin
admin.site.register(Promotions, PromotionsAdmin)
