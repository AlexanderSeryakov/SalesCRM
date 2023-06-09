from django.core.exceptions import ValidationError


def max_length_name(name: str):
    if len(name) > 20:
        raise ValidationError('Наименование товара не должно превышать 20 символов.')
    return name


def validate_price(price: [int, float]) -> float:
    """
    Function checks if the price is greater than 0

    if check is complete - return price,
    else raise ValidationError.

    :param price: [int, float]
    :return: price or ValidationError
    """
    if price <= 0:
        raise ValidationError('Цена должна быть больше 0')

    split_price = str(price).split('.')
    if len(split_price[1]) > 3 or len(split_price[0]) > 6:
        raise ValidationError('Введите цену в корректном формате. Максимальная цена 999999.99')

    return price


def try_to_get_price(cleaned_data: dict, key: str) -> float:
    """
    Function checks that key in cleaned_data.
    This is necessary to make sure that the value with
    which we want to work is really in the cleaned_data dictionary,
    otherwise you can get an KeyError exception during the application.

    Use this validator when field-1 needs to be validated with field-2 as well.

    :param cleaned_data: dict-object - cleaned_data from form instance.
    :param key: str
    :return: cleaned_data[key] or ValidateError
    """
    try:
        price = cleaned_data[key]
    except KeyError:
        raise ValidationError('Неверно указана розничная или закупочная стоимость.'
                              ' Стоимость должна быть указана в формате: 250 или 250.67')

    return price
