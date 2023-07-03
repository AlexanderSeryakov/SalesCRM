import re
from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'e-mail'}))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = 'Обязательное поле. ' \
                                    'Только латинские буквы, цифры, символы подчёркивания и дефис.'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = ['Пароль не должен содержать личную информацию',
                                      'Пароль не может быть короче 8 символов.',
                                      'Не используйте распространённые пароли.',
                                      'Пароль не может состоять только из цифр.']

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = 'Введите пароль для подтверждения.'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=self.cleaned_data.get('email')).exists():
            raise ValidationError('Пользователь с таким e-mail адресом уже существует.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.match('^[a-z0-9_-]{3,16}$', username) is None:
            raise ValidationError('Логин может содержать только строчные и заглавные латинские буквы, цифры'
                                  'а также символ подчёркивания и дефис. Логин не может быть короче 3 символов и '
                                  'длиннее'
                                  '16')
        return username


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))