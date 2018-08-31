from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^box/([0-9]+)', views.message_box, name='message-box')
    ]