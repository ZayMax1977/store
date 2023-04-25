from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.decorators.cache import cache_page

from users.views import (EmailVerificationView, UserLoginView,
                         UserRegistrationView, UserUpdateView, logout)

app_name = 'users'

urlpatterns = [
    path('login/', cache_page(60)(UserLoginView.as_view()), name='login'),

    path('register/', cache_page(60)(UserRegistrationView.as_view()), name='register'),
    path('profile/<int:pk>', login_required(UserUpdateView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<uuid:code>', cache_page(60)(EmailVerificationView.as_view()), name='email_verification'),

]
