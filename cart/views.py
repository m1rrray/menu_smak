from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import AddNewProductCart
from posts.models import Post


@csrf_exempt
@require_POST
def update_cart(request):
    cart = Cart(request)
    # print('sdfsdf')
    update_type = request.POST.get('update_quantity')
    product_id = request.POST.get('id')
    print(update_type, product_id)

    if update_type == 'plus':
        cart.add(int(product_id), quantity=1, update_quantity=True, operation=update_type)
    elif update_type == 'minus':
        cart.add(int(product_id), quantity=-1, update_quantity=True, operation=update_type)

    return JsonResponse({'status': 'success'})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Post, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


@csrf_exempt
def cart_add(request):
    cart = Cart(request)
    form = AddNewProductCart(request.POST)

    if form.is_valid():
        product_id = form.cleaned_data['product_id']
        quantity = form.cleaned_data['quantity']
        print(product_id, quantity)
        cart.add(int(product_id), quantity=quantity)
        return redirect('cart_detail')

        # cart.add()


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})
