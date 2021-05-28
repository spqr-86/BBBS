from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(
        verbose_name=_('Город'),
        max_length=128,
        unique=True,
    )
    is_primary = models.BooleanField(
        verbose_name=_('Приоритет вывода'),
        default=False,
    )

    class Meta:
        app_label = 'api'
<<<<<<< HEAD
        ordering = ['name']
=======
        ordering = ('name',)
>>>>>>> main
        verbose_name = _('Город')
        verbose_name_plural = _('Города')

    def __str__(self):
        return self.name
