from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^prof$', views.profile, name='profile'),
]