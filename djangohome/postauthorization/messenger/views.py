from django.contrib.auth.models import User
from django.shortcuts import render
from .models import MessageBox, Message


# Create your views here.

def index(request):
    user = request.user
    if hasattr(user, 'messenger_boxes'):
        messenger_boxes = user.messenger_boxes.all()
    return render(request, 'messenger/index.html', {'messenger_boxes': messenger_boxes})


def message_box(request, id_box):
    user = request.user
    box = MessageBox.objects.get(id=id_box)
    sms = Message()
    sms.message_text = 'Hello, it\'s first message'
    sms.save()
    sms.box = box

    if box.user == user:
        owner = user
    elif box.sender == user:
        owner = box.sender
    from django.http import HttpResponse
    return HttpResponse('Hello')
    # return render(request, 'messenger/sms.html', {'box': box, 'owner': owner})
