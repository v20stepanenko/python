from distutils.command.upload import upload

from django.db import models


class Category(models.Model):

    def __str__(self):
        return self.name

    parent_category = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):

    def __str__(self):
        return self.name

    img = models.ImageField(upload_to='img/', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
