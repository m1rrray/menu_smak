from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from users.models import Address
from .models import Post
from cart.forms import AddNewProductCart
# Create your views here.


def index(request):
    page = Post.objects.all()
    cart_product_form = AddNewProductCart()
    return render(request, 'index.html', {'page': page, 'cart_product_form': cart_product_form})


# def product_details(request, product_id):
#     product = Post.objects.get(id=product_id)
#     data = {
#         'picture': product.picture,
#         'title': product.title,
#         'caption': product.caption,
#         'price': product.price,
#         'weight': product.weight,
#     }
#     return JsonResponse(data)

