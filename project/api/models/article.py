from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    color = ColorField(
        verbose_name=_('Цвет'),
        default='#FF0000')

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    def __str__(self):
        return self.title
