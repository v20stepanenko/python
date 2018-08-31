from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('Название', max_length=20)
    client = models.CharField('Клиенты', max_length=20, blank=True)
    partnership = models.CharField('Парнеры', max_length=20, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    def __str__(self):
        return self.name

    manufacturer = models.ManyToManyField(Manufacturer, verbose_name='Производители')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='Родьтельская категория')
    name = models.CharField('Название категории', max_length=20)


class Product(models.Model):
    name = models.CharField('Название продукта', max_length=20)
    categories = models.ManyToManyField(Category, verbose_name='Категория')
    manufacturer = models.ManyToManyField(Manufacturer, verbose_name='Производители')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
