from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, null=True)
    body = models.TextField()
    title = models.CharField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)
    body = models.TextField()
    author = models.ForeignKey(User, null=True)
