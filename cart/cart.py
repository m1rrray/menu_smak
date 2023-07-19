from decimal import Decimal
from django.conf import settings
from posts.models import Post


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity=1, update_quantity=False, operation=''):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product = Post.objects.get(pk=product_id)
        if self.cart.get(str(product_id)) is None:
            self.cart[str(product_id)] = {'quantity': quantity,
                                          'price': str(product.price)}

        elif update_quantity and operation == 'plus':
            print('hey')
            if self.cart[str(product_id)]['quantity'] < 15:
                self.cart[str(product_id)]['quantity'] += 1
                print(self.cart)

        elif update_quantity and operation == 'minus':
            print('hui')
            if self.cart[str(product_id)]['quantity'] > 0:
                self.cart[str(product_id)]['quantity'] -= 1
            if self.cart[str(product_id)]['quantity'] == 0:
                del self.cart[str(product_id)]
        else:
            print('sdfsdfsdfsdf')
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Post.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            # item['price'] = Decimal(item['price'])
            item['total_price'] = int(item['price']) * int(item['quantity'])
            # item['picture'] = item['product'].picture
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """

        return sum(item['quantity'] for item in self.cart.values())
        # pass

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(int(item['price']) * int(item['quantity']) for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True