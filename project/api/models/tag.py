from django.db import models
from django.utils.translation import gettext as _


class Tag(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True,
    )

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.slug
