from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import User


class LoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ПОЧТАҢЫЗ же АТЫҢЫЗ',
        'id': 'login_username_email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'СЫР СӨЗҮҢҮЗ',
        'id': 'login_password',
    }))

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            # Проверяем, является ли ввод email'ом
            if '@' in username_or_email:
                try:
                    user = User.objects.get(email=username_or_email)
                    username = user.username
                except User.DoesNotExist:
                    raise forms.ValidationError("Бул почта табылган жок")
            else:
                username = username_or_email

            user = auth.authenticate(username=username, password=password)
            if user:
                self.user_cache = user
            else:
                raise forms.ValidationError("Туура эмес почта/аты же сыр сөз")

        return self.cleaned_data

class RegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Эки сырсөз дал келген жок!",
    }

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'АТЫҢЫЗ',
        'id': 'signup_username',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'ПОЧТАҢЫЗ',
        'id': 'signup_email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'СЫР СӨЗҮҢҮЗ',
        'id': 'signup_password1',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'СЫР СӨЗҮҢҮЗДҮ КАЙТАЛАҢЫЗ',
        'id': 'signup_password2',
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'image']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Атыңыз'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Почтаңыз'}),
        }