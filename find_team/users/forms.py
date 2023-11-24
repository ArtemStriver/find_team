from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, ModelForm, Textarea

from users.models import Answer


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


class AnswerForm(ModelForm):
    text = Textarea()

    class Meta:
        model = Answer
        fields = ['answer_author', 'answer_recipient', 'contacts', 'text']
