
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms


from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', "placeholder": 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username','password',)

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите логин'}))

    age = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите возраст'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'муж/жен'}))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': '+7XXXXXXXXXX'}))


    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','gender','age','phoneNumber','password1','password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'},),required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',"readonly": True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',"readonly": True}))
    age = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',"readonly": True}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',"readonly": True}))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','image','gender','age','phoneNumber',)