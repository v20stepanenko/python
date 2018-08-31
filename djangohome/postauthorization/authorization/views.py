from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from authorization.models import Profile
from post.models import Post
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def registration(request):
    user = request.user
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.data
            user = User.objects.create_user(username=data.get('username'), email=data.get('email'),
                                            password=data.get('password'))
            user.save()
        return redirect(reverse('log'))
    elif request.method == 'GET':
        return render(request, 'authorization/registration-form.html', {'form': RegistrationForm(), 'user': user})


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('main'))
    if request.method == 'GET':
        return render(request, 'authorization/login.html', {'form': LoginForm()})
    elif request.method == 'POST':
        user_data = LoginForm(request.POST).data
        username = user_data.get('username')
        password = user_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                return redirect(reverse('main'))
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            return HttpResponse("The username and password were incorrect.")


@csrf_exempt
def profile(request):
    user = request.user
    if request.method == 'GET':
        print(user.first_name)
        if not hasattr(user, 'profile'):
            p = Profile()
            user.profile = p
            user.save()
            p.save()
    elif request.method == 'POST':
        user.first_name = request.POST.get('first-name')
        user.last_name = request.POST.get('second-name')
        user.profile.link_fb = request.POST.get('facebook')
        user.profile.description = request.POST.get('description')
        user.profile.birth_day = request.POST.get('birth-day')
        new_password = request.POST.get('password')
        if new_password:
            user.set_password(new_password)
        user.profile.save()
        user.save()
    print(dir(user.profile.birth_day))
    return render(request, 'authorization/user.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def get_user_info(request):
    user = request.user
    return JsonResponse({'name': user.username, 'id': user.id}, safe=False)
