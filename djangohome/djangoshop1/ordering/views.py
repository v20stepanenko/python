from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from cart.cart import Cart
from ordering.form import CustomerForm
from ordering.models import Customer, Order, OrderPosition


def order(request):
    cart = Cart(request)
    if cart.get_summary_quantity() == 0:
        return redirect('main-page')
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'ordering/index.html', {'form': form, 'cart': cart})
    if request.method == 'POST':
        post = request.POST
        form = CustomerForm(request.POST)
        try:
            customer = Customer.objects.get(first_name=post.get('first_name'), last_name=post.get('last_name'),
                                            phone_number=post.get('phone_number'))
        except Customer.DoesNotExist as err:
            print(err)
            if {'first_name', 'last_name', 'phone_number'} < set(post.keys()):
                customer = Customer(first_name=post['first_name'], last_name=post['last_name'],
                                    phone_number=post['phone_number'])
                customer.save()
        if not customer:
            return JsonResponse({'message': 'error'})
        order = Order()
        order.status = 'made'
        order.address = post.get('address')
        order.customer = customer
        order.save()
        # print(customer)
        cart = Cart(request)
        for position in cart.get_products():
            order_position = OrderPosition()
            order_position.product = position['product']
            order_position.quantity = position['quantity']
            order_position.order = order
            order.save()
        print(order)
        return render(request, 'ordering/index.html', {'form': form, 'cart': cart})
