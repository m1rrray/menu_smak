from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/', views.cart_add, name='cart_add'),
    path('update/', views.update_cart, name='update_cart'),
    # path('apply_promotion/', views.apply_promotion, name='apply_promotion'),

    # path('add/', views.cart_add, name='cart_add'),
    # path('remove/<product_id>/$', views.cart_remove, name='cart_remove'),
]