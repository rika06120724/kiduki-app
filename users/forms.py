from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(
        error_messages={
            'required': 'メールアドレスを入力してください。',
            'invalid': '有効なメールアドレスを入力してください。',
            'unique': 'このメールアドレスは既に使用されています。',
        },
        widget=forms.EmailInput(attrs={
            'class': 'w-full h-12 border border-gray-400 rounded px-4',
        })
    )
    
    password1 = forms.CharField(
        error_messages={
            'required': 'パスワードを入力してください。',
        },
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-12 border border-gray-400 rounded px-4',
        })
    )
    
    password2 = forms.CharField(
        error_messages={
            'required': 'パスワード確認を入力してください。',
        },
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-12 border border-gray-400 rounded px-4',
        })
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        error_messages = {
            'password_mismatch': 'パスワードが一致しません。',
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='メールアドレス',
        error_messages={
            'required': 'メールアドレスを入力してください。',
            'invalid': '有効なメールアドレスを入力してください。',
        },
        widget=forms.EmailInput(attrs={
            'class': 'w-full h-12 border border-gray-400 rounded px-4',
        })
    )
    
    password = forms.CharField(
        label='パスワード',
        error_messages={
            'required': 'パスワードを入力してください。',
        },
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-12 border border-gray-400 rounded px-4',
        })
    )

    error_messages = {
        'invalid_login': 'メールアドレスまたはパスワードが正しくありません。',
    }