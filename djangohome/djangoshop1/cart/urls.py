from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='cart'),
    url(r'^add', views.add_product, name='add-products'),
    url(r'^clear', views.clear, name='clear-cart'),
    url(r'^clear-position', views.clear_position, name='clear-position'),
    url(r'^minus-products', views.minus_product, name='minus-products')
    ]
