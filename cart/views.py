from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import AddNewProductCart, UsePromotion
from posts.models import Post
from users.models import Order, OrderItem


# def apply_promotion(request):
#     if request.method == 'POST':
#         form = UsePromotion(request.POST)
#         if form.is_valid():
#             promocode = form.cleaned_data['promocode']
#             # Здесь вы можете использовать полученный промокод и выполнить нужные действия
#             # например, применить скидку к корзине или проверить его наличие в базе данных
#
#             # После выполнения нужных действий, вы можете вернуться на страницу корзины
#             return redirect('cart_detail')
#     else:
#         form = UsePromotion()
#
#     return render(request, 'cart.html', {'form': form})

@csrf_exempt
@require_POST
def update_cart(request):
    cart = Cart(request)
    update_type = request.POST.get('update_quantity')
    product_id = request.POST.get('id')
    # print(update_type, product_id)

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


    # Создание заказа
    order = Order.objects.create(user=request.user, total_price=cart.get_total_price_with_prom())


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
    # if request.method == 'POST':
    #     cart = Cart(request)
    #     user = request.user
    #     total_price = cart.get_total_price()
    #
    #     # Создаем экземпляр Order
    #     order = Order.objects.create(user=user, total_price=total_price)
    #
    #     # Получаем содержимое корзины
    #     cart_items = cart.cart.values()
    #
    #     # Добавляем блюда из корзины в модель OrderItem
    #     for item in cart_items:
    #         product_id = item['product_id']
    #         quantity = item['quantity']
    #         price = item['price']
    #
    #         order_item = OrderItem.objects.create(
    #             order=order,
    #             product=Post.objects.get(pk=product_id),
    #             quantity=quantity,
    #             price=price
    #         )
    #
    #     # Очищаем корзину
    #     cart.clear()
    #
    #     # Перенаправляем пользователя на страницу подтверждения заказа
    #     return redirect('profile')
    # return redirect("cart")
    # return render(request, 'cart.html', {'cart': cart})


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
