from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Teams(models.Model):
    # TODO сделать чтобы в качестве владельца был тот, кто создает команду.
    owner = models.ForeignKey('auth.User',
                              related_name='team_owner',
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)
    title = models.CharField('Название', max_length=42)
    intro = models.CharField('Вступление', max_length=250)
    text = models.TextField('Описание')
    # comrades = models.ManyToManyField('Связать с таблицей пользователей', related_name='comrades', blank=True)
    deadline = models.DateTimeField('Срок набора команды', default=datetime.now)
    tags = models.CharField('Категории', max_length=64)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/teams/{self.id}'

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
