from django.db import models
from django.utils.translation import gettext_lazy as _


class TextBlock(models.Model):
    text = models.TextField(
        verbose_name=_('Текст'),
    )
    order = models.PositiveSmallIntegerField(
        verbose_name=_('Порядок вывода'),
        default=0,
    )

    class Meta:
        app_label = 'common'
        ordering = ('order', )
        verbose_name = _('Блок текста')
        verbose_name_plural = _('Блоки текста')

    def __str__(self):
        return self.text[:25]
