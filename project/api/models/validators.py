from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def age_validator(value):
    if value > 25:
        raise ValidationError(
            _('Упс.. ребенок уже слишком взрослый'),
            code='invalid',
            params={'value': value},
        )