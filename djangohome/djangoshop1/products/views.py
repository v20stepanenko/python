from django.shortcuts import render

# Create your views here.
from products.models import Product, Category


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', {'product': product})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.product_set.all()
    context = {'products': products}
    return render(request, 'products/category.html', context)
