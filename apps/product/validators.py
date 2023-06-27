from django.core.exceptions import ValidationError


def is_positive_price(price: [int, float]) -> [int, float]:
    """
    Function checks if the price is greater than 0

    if check is complete - return price,
    else raise ValidationError.

    :param price: [int, float]
    :return: price or ValidationError
    """
    if price > 0:
        return price
    raise ValidationError('Цена должна быть больше 0')
