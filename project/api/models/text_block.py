from django.db import models
from django.utils.translation import gettext_lazy as _


class TextBlock(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    text = models.TextField(
        verbose_name=_('Текст'),
    )
    order = models.PositiveSmallIntegerField(
        verbose_name=_('Порядок вывода'),
        default=0,
    )

    class Meta:
        app_label = 'api'
        ordering = ('order', )
        verbose_name = _('Абзац')
        verbose_name_plural = _('Абзацы')

    def __str__(self):
        return self.title
