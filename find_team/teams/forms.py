import datetime

from .models import Teams
from django.forms import ModelForm, TextInput, Textarea, DateInput, DateTimeField


class TeamsForm(ModelForm):
    deadline = DateTimeField(required=False,
                             widget=DateInput(attrs={'type': 'datetime-local',
                                                     'class': 'form-control',
                                                     'placeholder': "Крайний срок для сбора команды"}),
                             initial=datetime.date.today(),
                             localize=True)

    class Meta:
        model = Teams
        fields = ['owner', 'title', 'intro', 'text', 'tags']

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
            'tags': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Теги для быстрого поиска"
            })
        }
