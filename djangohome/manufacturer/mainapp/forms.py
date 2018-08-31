from django.forms import ModelForm
from .models import Category, Product, Manufacturer


class NewManufactrurerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'client', 'partnership']


class NewCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'manufacturer', 'parent_category']


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'manufacturer', 'categories']
