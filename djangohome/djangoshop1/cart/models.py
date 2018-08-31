from django.db import models

from products.models import Product


class Cart(models.Model):
    pass


class CartPosition(models.Model):
    product = models.OneToOneField(Product)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart)