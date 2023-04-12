from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render
from django.urls import reverse

from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    """
    функция получает данные из формы авторизации или отрисовывает страницу авторизвции
    """
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request,user)
                return  HttpResponseRedirect('/')

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request,'users/login.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегестрировались.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request,'users/register.html',context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Store - Профиль',
        'form': form,
        'basket': Basket.objects.filter(user=request.user)
    }
    return render(request,'users/profile.html',context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))