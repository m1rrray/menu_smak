from django.shortcuts import render

from cart.forms import AddNewProductCart
from .models import Post


def index(request):
    page = Post.objects.all()
    cart_product_form = AddNewProductCart()
    return render(request, 'index.html', {'page': page, 'cart_product_form': cart_product_form})
