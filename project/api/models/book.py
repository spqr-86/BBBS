from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ..fields import fields


class Book(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    info = models.CharField(
        verbose_name=_('Информация'),
        max_length=256,
    )
    annotation = models.TextField(
        verbose_name=_('Аннотация'),
        max_length=1024,
    )
    color = fields.ColorField(
        verbose_name=_('Цвет'),
        default='#FF0000',
    )
    tags = models.ManyToManyField(
        'api.Tag',
        verbose_name=_('Теги'),
        related_name='books',
    )

    def colortile(self):
        if self.color:
            return format_html('<div style="background-color: {0}; \
                height: 100px; width: 100px"></div>', self.color)
        return 'пусто'

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Книга')
        verbose_name_plural = _('Книги')

    def __str__(self):
        return self.title
