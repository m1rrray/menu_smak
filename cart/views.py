from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import AddNewProductCart, UsePromotion
from posts.models import Post
from users.models import Order, OrderItem

import json


@csrf_exempt
@require_POST
def update_cart(request):
    cart = Cart(request)
    update_type = request.POST.get('update_quantity')
    product_id = request.POST.get('id')

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


@csrf_exempt
def place_order(request):
    cart = Cart(request)
    print(request.POST)
    post_data = json.loads(list(request.POST.keys())[0])
    cart_price = post_data.get('cartPrice')

    # Создание заказа
    order = Order.objects.create(user=request.user, total_price=cart_price)

    # Сохранение содержимого заказа
    for item in cart:
        product = item['product']
        quantity = item['quantity']
        price = item['price']
        OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

    # Очистка корзины после оформления заказа
    cart.clear()

    # Возвращение JSON-ответа с ID созданного заказа или сообщением об успешном создании заказа
    return JsonResponse({'order_id': order.id, 'message': 'Заказ успешно создан'})


def cart_detail(request):
    cart = Cart(request)
    form = UsePromotion(request.POST or None)  # Создаем форму и передаем в нее данные из POST запроса
    if request.method == 'POST' and form.is_valid():
        promocode = form.cleaned_data['promocode']
        cart.set_promocode(promocode)  # Применяем промокод к корзине

    user = request.user

    # Получить последний адрес пользователя, если он есть
    last_address = None
    if user.addresses.exists():
        last_address = user.addresses.last()

    random_posts = list(Post.objects.order_by('?')[:4])

    return render(request, 'cart.html', {'cart': cart, 'form': form, 'last_address': last_address,
                                         'random_posts': random_posts})
