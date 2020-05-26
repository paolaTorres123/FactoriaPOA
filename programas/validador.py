from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def validate_es_entero(value):
    try:
        return int(value)

    except ValueError:
        raise ValidationError(
            _('Formato inválido validador'),
        )
