from django.db import models
from django.utils.translation import gettext_lazy as _


class History(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    image_url = models.URLField(
        verbose_name=_('Изображение'),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'api'
        verbose_name = _('История')
        verbose_name_plural = _('Истории')

    def __str__(self):
        return self.title
