from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


def events_lifetime_validator(event):
    if event.end_at <= now():
        raise ValidationError(
            _('Событие "%(event)s" уже закончилось'),
            code='invalid',
            params={'event': event},
        )


def free_seats_validators(event):
    if event.participants.count() >= event.seats:
        raise ValidationError(
            _('Все места на "%(event)s" уже заняты'),
            code='invalid',
            params={'event': event},
        )


def age_validator(value):
    if value > 25:
        raise ValidationError(
            _('Слишком большой возраст для ребёнка'),
            code='invalid',
            params={'value': value})
    elif value < 0:
        raise ValidationError(
            _('Возраст не может быть меньше 0'),
            code='invalid',
            params={'value': value})


def year_validator(value):
    if value > now().year:
        raise ValidationError(
            '%(value)s год больше текущего',
            code='invalid',
            params={'value': value},
        )
