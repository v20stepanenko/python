from django.contrib.auth.models import User
from django.db import models


class MessageBox(models.Model):
    user = models.ForeignKey(User, related_name='messenger_boxes')
    sender = models.OneToOneField(User, related_name='sender')


class Message(models.Model):
    box = models.ForeignKey(MessageBox, null=True)
    message_text = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
    is_response = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
