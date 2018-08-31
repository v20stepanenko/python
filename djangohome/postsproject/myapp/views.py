from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from myapp.forms import PostForm
from .models import Post


def all_posts(request):
    posts = Post.objects.all()
    text = ['<h2>Список постов</h2><hr><ul>']
    for post in posts:
        text.append('<a href="/posts/post{0}"><li>{1}</li></a>'.format(post.id, post.title))
    text.append('</ul> ')
    data = ''.join(text)
    return HttpResponse(data)


def simple_post(request, post_id):
    post = Post.objects.get(id=post_id)
    data = '<h2>{0}</h2><p>{1}</p><p>{2}</p>'.format(post.title, post.text, post.author)
    return HttpResponse(data)


def post_form(request):
    if request.method == 'GET':
        f = PostForm()
        context = {'postform': f}
        return render(request, 'myapp/post.html', context)
    if request.method == 'POST':
        f = PostForm(request.POST)
        if f.is_valid():
            f.save()
        return redirect(reverse('all posts'))


def counter(request):
    if not request.session.get('counter'):
        request.session['counter'] = 1
    else:
        c = request.session['counter']
        c += 1
        request.session['counter'] = c
    return HttpResponse(request.session['counter'])
