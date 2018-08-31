from django.conf.urls import url, include
from django.contrib import admin
import authorization.views as auth_views
import post.views as post_views

urlpatterns = [
    url(r'^$', post_views.index, name='main'),
    url(r'^post/', include('post.urls')),
    url(r'^reg$', auth_views.registration, name='reg'),
    url(r'^log$', auth_views.login_user, name='log'),
    url(r'^logout$', auth_views.logout_user, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^user-info', auth_views.get_user_info, name='get-user-info'),
    url(r'^user-message/', include('messenger.urls')),
    url(r'^user/', include('authorization.urls'))
    ]
