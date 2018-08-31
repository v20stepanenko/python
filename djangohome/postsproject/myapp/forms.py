from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    datetime = forms.DateTimeField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'datetime']
