from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=50)
    datetime = models.DateTimeField(null=True)
