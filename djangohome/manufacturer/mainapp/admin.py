from django.contrib import admin
from .models import Product, Manufacturer, Category

admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Category)

# class InlineManufactory(admin.TabularInline):
#     model = Book
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [InlineBook]
#
#
# admin.site.register(Author, AuthorAdmin)
