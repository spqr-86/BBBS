from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    tags = models.ManyToManyField(
        'api.Tag',
        verbose_name=_('Тег'),
        related_name='questions',
    )

    class Meta:
        app_label = 'api'
        ordering = ['id']
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.title
