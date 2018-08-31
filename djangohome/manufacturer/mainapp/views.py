from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from .forms import NewManufactrurerForm, NewCategoryForm, NewProductForm
from .models import Category, Manufacturer, Product


def get_products_all():
    return Product.objects.all()


def get_manufacturers_all():
    return Manufacturer.objects.all()


def get_categories_all():
    return Category.objects.all()


def index(request):
    template = loader.get_template('mainapp/index.html')
    context = {
        'categories': get_categories_all(),
        'manufactures': get_manufacturers_all(),
        'products': get_products_all()
        }
    return HttpResponse(template.render(context))


def category(request, id_category):
    context = {
        'categories': get_categories_all(),
        'category': Category.objects.get(id=id_category),
        'products': get_products_all(),
        'manufactures': get_manufacturers_all()
        }
    return render(request, 'mainapp/category.html', context)


def category_by_manufacturer(request, id_category, id_manufacturer):
    manufacturer = Manufacturer.objects.get(id=id_manufacturer)
    categories = manufacturer.category_set.all()
    category = manufacturer.category_set.filter(id=id_category).first()
    products = category.product_set.all() if category else None
    context = {
        'manufacturer': manufacturer,
        'categories': categories,
        'category': category,
        'products': products
        }
    return render(request, 'mainapp/category-manufacturer.html', context)


def category_manufacturer_product(request, id_category, id_manufacturer, id_product):
    product = Manufacturer.objects.get(id=id_manufacturer).product_set.get(id=id_product) or None
    context = {
        'product': product
        }
    return render(request, 'mainapp/', context)


def product(request, id_product):
    product = Product.objects.get(id=id_product)
    return render(request, 'mainapp/product.html', {'product': product})


def manufacturer(request, id_manufacturer):
    manufacturer = Manufacturer.objects.get(id=id_manufacturer)
    context = {
        'manufacturer': manufacturer,
        'products': manufacturer.product_set.all(),
        'categories': manufacturer.category_set.all()
        }
    return render(request, 'mainapp/manufacturer.html', context)


def new_product(request):
    if request.method == 'POST':
        response = NewProductForm(request.POST)
        if response.is_valid():
            response.save()
        return redirect(reverse('categories'))

    elif request.method == 'GET':
        form = NewProductForm()
        context = {'product_form': form}
        return render(request, 'mainapp/newproduct.html', context)


def new_category(request):
    if request.method == 'POST':
        response = NewCategoryForm(request.POST)
        if response.is_valid():
            response.save()
        return redirect(reverse('categories'))

    elif request.method == 'GET':
        form = NewCategoryForm()
        context = {'category_form': form}
        return render(request, 'mainapp/newcategory.html', context)


def new_manufacturer(request):
    if request.method == 'POST':
        response = NewManufactrurerForm(request.POST)
        if response.is_valid():
            response.save()
        return redirect(reverse('categories'))

    elif request.method == 'GET':
        form = NewManufactrurerForm()
        context = {'manufacturer_form': form}
        return render(request, 'mainapp/newmanufacturer.html', context)
