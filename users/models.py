from django.db import models


class Answer(models.Model):
    """Модель ответа на заявку."""
    answer_author = models.ForeignKey('auth.User',
                                      related_name='answer_author',
                                      on_delete=models.CASCADE,
                                      blank=True,
                                      null=True)
    answer_recipient = models.IntegerField('ID получателя ответа', blank=True, null=True)
    contacts = models.CharField('Контакты', max_length=42)
    text = models.TextField('Информация для заявителя')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
