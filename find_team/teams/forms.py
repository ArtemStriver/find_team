import datetime

from .models import Teams
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateInput


class TeamsForm(ModelForm):
    class Meta:
        model = Teams
        fields = ['title', 'intro', 'text', 'deadline', 'tags']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Заголовок для команды"
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Краткое описание команды"
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Подробное описание команды"
            }),
            'deadline': DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Крайний срок для сбора команды"
                }),
            'tags': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Теги для быстрого поиска"
            })
        }
