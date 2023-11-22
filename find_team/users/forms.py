from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', )

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Логин"
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Логин"
            }),
        }
