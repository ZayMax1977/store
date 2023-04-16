from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import  logout, UserRegistrationView, UserUpdateView, UserLoginView

app_name = 'users'

urlpatterns = [
    # path('login/', login, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', login_required(UserUpdateView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),

]