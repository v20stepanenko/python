from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^([0-9]+)', views.product, name='show-product'),
    url(r'^category/([0-9]+)', views.category, name='category')
    ]
