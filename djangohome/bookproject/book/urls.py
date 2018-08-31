from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.general_info, name='info'),
    url(r'^author([0-9])+', views.author, name='author books'),  # что такое параметр name?
    url(r'^book([0-9])+', views.book, name='book'),
    ]
