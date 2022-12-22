from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from posts.validators import tags_validator


class SignupForm(forms.Form):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'tags'}),
        validators=[tags_validator],
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
