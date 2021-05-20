from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(
        verbose_name=_('Город'),
        max_length=128,
    )

    class Meta:
        app_label = 'api'
        ordering = ['id']
        verbose_name = _('Город')
        verbose_name_plural = _('Города')

    def __str__(self):
        return self.name
