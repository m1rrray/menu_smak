from django.shortcuts import render
from .models import Post
from cart.forms import AddNewProductCart
# Create your views here.


def index(request):
    page = Post.objects.all()
    cart_product_form = AddNewProductCart()
    return render(request, 'index.html', {'page': page, 'cart_product_form': cart_product_form})

