import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .cart import Cart


# Create your views here.

def get_product_id_json(request):
    request_body = json.loads(request.body)
    return request_body.get('product_id')


def index(request):
    cart = Cart(request)
    if cart.get_summary_quantity() == 0:
        return redirect('main-page')
    return render(request, 'cart/index.html', {'cart': cart})


@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart.add_product(get_product_id_json(request))
        return JsonResponse({'summary_quantity': cart.get_summary_quantity()}, safe=False)


@csrf_exempt
def minus_product(request):
    if request.method == 'PUT':
        cart = Cart(request)
        cart.minus_product(get_product_id_json(request))
    return JsonResponse({'message': 'minus'})


@csrf_exempt
def clear_position(request):
    if request.method == 'PUT':
        cart = Cart(request)
        cart.clear_position(get_product_id_json(request))
    return JsonResponse({'message': 'clear-position'})


@csrf_exempt
def clear(request):
    if request.method == 'DELETE':
        cart = Cart(request)
        cart.clear()
    return JsonResponse({'message': 'clear-cart'})
