from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'([a-zA-Z0-9]+)-([a-zA-Zа-яА-Я0-9]+)', views.get_address, name='addresses')
    ]
