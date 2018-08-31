from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='categories'),
    url(r'^([0-9]+)$', views.category, name='category'),
    url(r'^([0-9]+)/manufacturer/([0-9]+)$', views.category_by_manufacturer, name='category-by-manufacturer'),
    url(r'^([0-9]+)/manufacturer/([0-9]+)/product/([0-9]+)$', views.category_manufacturer_product, name='category-manufacturer-product'),

    ]


