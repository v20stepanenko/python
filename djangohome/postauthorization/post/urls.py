from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([0-9]+)$', views.get_post, name='post'),
    url(r'^create$', views.create_post, name='create-post'),
    url(r'^comment/create$', views.create_comment, name='create-comment'),
    url(r'^([0-9]+)/comments', views.comments_by_post_id, name='get-comments'),
    url(r'^comment/del/([0-9]+)$', views.del_comment, name='del-comment'),
    url(r'^user$', views.posts_user, name='posts-user'),
    url(r'^user/([0-9]+)$', views.show_user, name='show-user'),
    url(r'^all$', views.all_posts, name='get-posts')
    ]
