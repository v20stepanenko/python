from django.http import HttpResponse
from django.template import loader
from .models import Book, Author


def general_info(request):
    template = loader.get_template('book/index.html')
    context = {
        'authors': Author.objects,
        'books': Book.objects,
        }
    return HttpResponse(template.render(context))


def author(request, id_author):
    template = loader.get_template('book/author.html')
    author = Author.objects.get(id=id_author)
    books = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books': books
        }
    return HttpResponse(template.render(context))


def book(request, id_book):
    template = loader.get_template('book/book.html')
    book = Book.objects.get(id=id_book)
    context = {
        'book': book
        }
    return HttpResponse(template.render(context))
