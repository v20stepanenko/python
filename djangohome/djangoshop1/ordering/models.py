from django.core.validators import RegexValidator
from django.db import models

from cart.models import Cart
from products.models import Product


class Customer(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    class Meta:
        unique_together = ('first_name', 'last_name', 'phone_number')


class Order(models.Model):
    STATUS_CHOICES = (
        ('made', 'оформленый'),
        ('approved', 'подтвержденный'),
        ('mailed', 'отправленый'),
        ('paid', 'оплаченый')
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    address = models.CharField(max_length=1024)
    data = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderPosition:
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
