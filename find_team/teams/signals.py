from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Teams


@receiver(pre_save, sender=Teams)
def set_owner(sender, instance, **kwargs):
    # Проверяем, если owner не установлен
    if not instance.owner:
        # Присваиваем owner текущего авторизованного пользователя
        instance.owner = User.objects.get(username='User.username')
