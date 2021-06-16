from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
