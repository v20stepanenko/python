import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment
from .forms import NewPostForm


def index(request):
    
    return render(request, 'post/index.html')




def create_post(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            assert request.POST.get('body') and request.POST.get('title')
            user_post = Post()
            user_post.body = request.POST.get('body')
            user_post.title = request.POST.get('title')
            user_post.save()
            user_post.author = user
            user_post.save()
            return redirect(reverse('posts-user'))
        if request.method == 'GET':
            form = NewPostForm()
            return render(request, 'post/newpost.html', {'user': user, 'form': form})


@csrf_exempt
def create_comment(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            request_site = json.loads(request.body)
            assert request_site.get('body')
            assert request_site.get('post_id')
            user_comment = Comment()
            user_comment.body = request_site.get('body')
            user_comment.save()
            user_comment.author = user
            user_comment.post = Post.objects.get(id=request_site.get('post_id'))
            user_comment.save()
            return JsonResponse({'message': 'ok'}, safe=False)


def del_comment(request, comment_id):
    user = request.user
    comment = Comment.objects.get(id=comment_id)
    if user == comment.author or user == comment.post.author:
        comment.delete()
    return index(request)


def posts_user(request):
    return render(request, 'post/user.html')


def show_user(request, id_user):
    user_by_id = User.objects.get(id=id_user)
    return render(request, 'post/user.html', {'user2': user_by_id})


def all_posts(request):
    posts = Post.objects.all()
    response = []
    for post in posts:
        response.append({'post_id': post.id,
                         'post_body': post.body,
                         'post_title': post.title,
                         'post_author': {'name': post.author.username, 'id': post.author.id}})
    return JsonResponse(response, safe=False)


def get_post(request, id_post):
    post = Post.objects.get(id=id_post)
    return render(request, 'post/post.html', {'post': post})


@csrf_exempt
def comments_by_post_id(request, post_id):
    if request.method == 'POST':
        return JsonResponse({'message': 'Anonymus'})
    user = request.user
    if user.is_authenticated():
        post = Post.objects.get(id=post_id)
        comments = []
        for prepare in post.comment_set.all():
            can_del = False
            if prepare.author == user or post.author == user:
                can_del = True
            comments.append({'can_del': can_del, 'comment_id': prepare.id,
                             'author': {'name': prepare.author.username, 'id': prepare.author.id},
                             'body': prepare.body})
        return JsonResponse(comments, safe=False)
    else:
        return JsonResponse({'message': 'Anonymus'})
