from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse('users:register')
        self.data = {
            'first_name': 'miroslav',
            'last_name': 'miroslav',
            'username': 'miroslav',
            'email': 'zamax77@mail.ru',
            'age': '21',
            'gender': 'm',
            'phoneNumber': '+79182736553',
            'password1': '1977miroslav1977',
            'password2': '1977miroslav1977'

        }

# проверка на отрисовку (get запрос)

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK, "Статус кода не 200")
        self.assertEqual(response.context_data['title'], 'Store - Регистрация', 'Title - не прошел')
        self.assertTemplateUsed(response, 'users/register.html', 'ПРОВЕРКА template_name НЕ ПРОШЛА')

# проверка проходит ли регистрация
    def test_user_registration_post_success(self):

        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND, "Статус кода не 302")
        self.assertRedirects(response,reverse('users:login'))
        # проверяем существует ли пользователь с username объявленном выше, если будет
        # True То проверка на создание пользователя прошла
        self.assertTrue(User.objects.filter(username=username).exists())




