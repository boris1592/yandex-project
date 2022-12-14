from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.Form):
    username = forms.EmailField(
        label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password_repeat = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password_repeat'] != cleaned_data['password']:
            raise ValidationError('Повтор пароля не совпадает с паролем')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
