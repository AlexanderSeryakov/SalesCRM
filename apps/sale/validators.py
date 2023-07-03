import re

from django.core.exceptions import ValidationError


def validate_phone_number(phone_number: str) -> [str, None]:
    """
    Function validate phone number and replace all symbols '-' to empty string ''.

    :param phone_number: str
    :return: phone number or ValidateError
    """

    if phone_number is None:
        return phone_number

    result = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                      phone_number)

    if result:
        phone_number = phone_number.replace('-', '').replace('+', '')
        return phone_number

    raise ValidationError('Введите номер телефона в корректном формате. Например: 8-800-100-00-00 или 88001000000.')


def quantity_in_allow_range(quantity: int) -> None:
    if not 0 < quantity < 101:
        raise ValidationError('Количество не может превышать 100 единиц и не может быть меньше 1.')
