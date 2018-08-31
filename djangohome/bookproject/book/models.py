from django.db import models


class Author(models.Model):

    def __str__(self):
        return self.name + ' ' + self.surname

    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_books(self):
        return Book.objects.filter(author=self)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    book_name = models.CharField('Название книги', max_length=10)
    release_data = models.DateField('Дата релиза')
