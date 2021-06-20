from django.db import models
from django.utils.translation import gettext_lazy as _


class Catalog(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Справочник')
        verbose_name_plural = _('Справочник')

    def __str__(self):
        return self.title
