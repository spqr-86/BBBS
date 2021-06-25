from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ..fields import fields
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
    color = fields.ColorField(
        verbose_name=_('Цвет'),
        default='#FF0000',
    )
    image_url = models.URLField(
        verbose_name=_('Изображение'),
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='rights/',
        verbose_name=_('Фото'),
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        'api.Tag',
        verbose_name=_('Тег(и)'),
        related_name='rights',
    )

    def colortile(self):
        if self.color:
            return format_html('<div style="background-color: {0}; \
                height: 100px; width: 100px"></div>', self.color)
        return 'пусто'

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Право')
        verbose_name_plural = _('Права')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        if self.image_url and not self.image:
            self.load_image(image_url=self.image_url)
        return super().save(*args, **kwargs)
