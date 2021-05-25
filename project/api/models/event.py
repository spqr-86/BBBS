from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Event(models.Model):
    address = models.CharField(
        verbose_name=_('Адрес мероприятия'),
        max_length=200,
    )
    contact = models.CharField(
        verbose_name=_('Контактное лицо'),
        max_length=200,
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    description = models.TextField(
        verbose_name=_('Описание мероприятия'),
        max_length=1000,
    )
    start_at = models.DateTimeField(
        verbose_name=_('Время начала'),
    )
    end_at = models.DateTimeField(
        verbose_name=_('Время окончания'),
    )
    seats = models.PositiveSmallIntegerField(
        verbose_name=_('Максимальное число участников'),
        validators=[validators.MinValueValidator(1)],
    )
    city = models.ForeignKey(
        'api.City',
        verbose_name=_('Город мероприятия'),
        related_name='events',
        on_delete=models.PROTECT,
    )
    participants = models.ManyToManyField(
        User,
        through='Participant',
        through_fields=('event', 'participant'),
        verbose_name=_('Участники'),
        related_name='events',
    )

    class Meta:
        app_label = 'api'
        ordering = ['id']
        verbose_name = _('Событие')
        verbose_name_plural = _('События')

    def clean(self):
        errors = {}
        if self.start_at > self.end_at:
            errors['end_at'] = ValidationError(
                _('Конец события не может быть раньше начала'))
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.title


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'api'
        ordering = ['id']
        verbose_name = _('Участник')
        verbose_name_plural = _('Участники')
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'participant'],
                name='event_participant_uniquetogether',
            )
        ]

    def clean(self):
        errors = {}
        if not self.event:
            errors['event'] = ValidationError(
                _('Укажите событие'))
        if self.event.end_at <= datetime.now(timezone.utc):
            errors['event'] = ValidationError(
                _('Событие уже закончилось'))
        if errors:
            raise ValidationError(errors)
