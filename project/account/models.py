from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
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
    curator = models.ForeignKey(
        to='CustomUser',
        verbose_name=_('Куратор'),
        related_name='mentors',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.username}: {self.first_name} {self.last_name[:1]}.'
        return self.username

    def clean(self):
        errors = {}
        if self.curator is None and self.is_mentor:
            errors['curator'] = ValidationError(
                _('У наставника должен быть куратор'))
        if self.curator is not None and not self.is_mentor:
            errors['curator'] = ValidationError(
                _('Куратор может быть только у наставника'))
        if self.is_mentor and self.city is None:
            errors['city'] = ValidationError(
                _('У наставника должен быть город'))
        if errors:
            raise ValidationError(errors)
