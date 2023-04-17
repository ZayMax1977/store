from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User, EmailVerification


class UserLoginView(TitleMixin,LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'

    def get_success_url(self):
        return reverse_lazy('products:index')

class UserRegistrationView(TitleMixin,SuccessMessageMixin,CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    title = 'Store - Регистрация'
    success_message = 'Поздравляем! Вы успешно зарегестрировались.'

class UserUpdateView(TitleMixin,UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile',args =(self.object.id,))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

class EmailVerificationView(TitleMixin,TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self,request,*args,**kwargs):
        code = kwargs['code']
        user = User.objects.get(email = kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user,code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True

            user.save()
            return super(EmailVerificationView,self).get(request,*args,**kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))