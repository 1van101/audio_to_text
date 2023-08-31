from django.core.exceptions import ValidationError


def only_letters_validator(text):
    if not text.isalpha():
        raise ValidationError('Must contain only letters')