from django.shortcuts import render
from products.products import get_products
from products.models import Category, Product
from cart.cart import Cart

# Create your views here.


def index(request, from_prod=0, to_prod=10):
    products = get_products(from_prod, to_prod)
    quantity = Cart(request).get_summary_quantity()
    main_category = Category.objects.filter(parent_category__category__isnull=True)
    context = {'products': products, 'quantity': quantity, 'categories': main_category}
    return render(request, 'main/index.html', context)
