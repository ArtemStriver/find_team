# Generated by Django 4.2.7 on 2023-11-24 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_recipient', models.IntegerField(blank=True, null=True, verbose_name='ID получателя ответа')),
                ('contacts', models.CharField(max_length=42, verbose_name='Контакты')),
                ('text', models.TextField(verbose_name='Информация для заявителя')),
                ('answer_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]