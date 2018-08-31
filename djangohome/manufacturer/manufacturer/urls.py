from django.conf.urls import include, url
from django.contrib import admin
from mainapp import views as main_views

mainapp_urls = include('mainapp.urls')

urlpatterns = [
    url(r'^test', main_views.product, name='test'),
    url(r'^categories/', mainapp_urls),
    url(r'^category/', mainapp_urls),
    url(r'^admin/', admin.site.urls),
    url(r'^product/([0-9]+)$', main_views.product, name='product'),
    url(r'^manufacturer/([0-9]+)', main_views.manufacturer, name='manufacturer'),
    url(r'^newproduct/', main_views.new_product, name='new-product'),
    url(r'^newcategory/', main_views.new_category, name='new-category'),
    url(r'^newmanufacturer/', main_views.new_manufacturer, name='new-manufacturer')
    ]
