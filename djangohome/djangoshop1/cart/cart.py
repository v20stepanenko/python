from products.models import Product


def save(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        args[0].request.session['cart'] = args[0].cart

    return wrapper


class Cart:

    def __init__(self, request):
        self.request = request
        cart = request.session.get('cart')
        if cart:
            self.cart = cart.copy()
        else:
            self.cart = []

    @save
    def add_product(self, product_id):
        for position in self.cart:
            if position['product_id'] == product_id:
                position['quantity'] += 1
                return
        self.cart.append({'product_id': product_id, 'quantity': 1})  # if in for loop didn't found need products, create

    @save
    def del_product(self, product_id):
        for index in len(self.cart):
            position = self.cart[index]
            if position['product_id'] == product_id:
                self.cart.pop(index)

    @save
    def set_product_quantity(self, product_id, quantity):
        for position in self.cart:
            if position['product_id'] == product_id:
                position['quantity'] = quantity

    @save
    def clear(self):
        self.cart = []

    def get_summary_quantity(self):
        list_quantity = [position['quantity'] for position in self.cart]
        return sum(list_quantity)

    def get_total_price(self):  # можно ли под этот метот писать свой менеджер что бы бд сразу возращала цену?
        total_price = 0
        for position in self.cart:
            product_price = Product.objects.get(id=position.get('product_id')).price
            price_position = product_price * position.get('quantity')
            total_price += price_position
        return total_price

    def get_products(self):
        def maker_list(position):
            return {'product': Product.objects.get(id=position.get('product_id')), 'quantity': position['quantity']}

        return list(map(maker_list, self.cart))

    @save
    def minus_product(self, product_id):
        for position in self.cart:
            if position['product_id'] == product_id:
                if position['quantity'] > 1:
                    position['quantity'] -= 1
                else:
                    self.clear_position(product_id)
                return

    @save
    def clear_position(self, product_id):
        for position in self.cart:
            if position['product_id'] == product_id:
                self.cart.remove(position)
