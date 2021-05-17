from django.db import models
from django.utils.translation import gettext as _


class Place(models.Model):
    title = models.CharField(
        verbose_name=_('Заглавие'),
        max_length=200,
    )
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=200,
    )
    info = models.CharField(
        verbose_name=_('Информация'),
        max_length=500,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
    )
    imageUrl = models.URLField(
        verbose_name=_('Изображение'),
        blank=True,
        null=True,
    )
    link = models.URLField(
        verbose_name=_('Ссылка'),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'api'
        verbose_name = _('Место')
        verbose_name_plural = _('Места')

    def __str__(self):
        return self.title
