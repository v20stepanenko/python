from django.contrib import admin
from .models import Author, Book


class InlineBook(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [InlineBook]


admin.site.register(Author, AuthorAdmin)
