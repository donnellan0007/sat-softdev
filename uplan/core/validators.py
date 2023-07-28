from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_existence(value):
    # checks if value is empty
    if value == '':
        raise ValidationError(
            _("Field cannot be empty"),
            params={"value": value},
        )