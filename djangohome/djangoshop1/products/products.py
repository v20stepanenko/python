from .models import Product


def get_products(from_num, to_num):
    return Product.objects.all()[from_num:to_num]


def get_product(id_product):
    return Product.objects.get(id=id_product)


def get_products_by_category():
    pass
