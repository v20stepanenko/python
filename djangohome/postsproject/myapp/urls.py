from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_posts, name='all posts'),
    url(r'^form', views.post_form),
    url(r'^counter', views.counter),
    url(r'^post([0-9])+', views.simple_post, name='get post')  # что такое параметр name?
    ]

