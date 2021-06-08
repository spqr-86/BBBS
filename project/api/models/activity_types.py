from django.db import models
from django.utils.translation import gettext_lazy as _


class ActivityType(models.Model):
    name = models.CharField(
        verbose_name=_('Вид активности'),
        max_length=200
    )
