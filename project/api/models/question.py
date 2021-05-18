from django.db import models
from django.utils.translation import gettext_lazy as _

from .tag import Tag


class Question(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    tags = models.ForeignKey(
        Tag,
        verbose_name=_('Тег'),
        related_name='question',
        on_delete=models.CASCADE
    )

    class Meta:
        app_label = 'api'
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.title
