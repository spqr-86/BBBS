from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import ImageFromUrlMixin


class Right(models.Model, ImageFromUrlMixin):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    description = models.CharField(
        verbose_name=_('Описание'),
        max_length=500,
    )
    text = models.TextField(
        verbose_name=_('Текст'),
    )
    raw_html = models.TextField(
        verbose_name=_('HTML'),
        max_length=4 * 10 ** 6,
        help_text=_('Поле для html кода страницы.'),
    )
    tags = models.ManyToManyField(
        'api.Tag',
        verbose_name=_('Тег(и)'),
        related_name='rights',
        limit_choices_to={'category': _('Права')},
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Право')
        verbose_name_plural = _('Права')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.raw_html = ' '.join(self.raw_html.split())
        return super().save(*args, **kwargs)
