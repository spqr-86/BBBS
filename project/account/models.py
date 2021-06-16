from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    city = models.ForeignKey(
        'api.City',
        verbose_name=_('Город'),
        related_name='users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    region = models.ForeignKey(
        'api.Region',
        verbose_name=_('Регион'),
        related_name='users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    is_mentor = models.BooleanField(
        verbose_name=_('Наставник'),
        default=False,
    )
