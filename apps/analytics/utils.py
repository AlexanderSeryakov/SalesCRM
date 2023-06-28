from datetime import datetime

from apps.sale.models import Sale


def get_valid_data_for_template(user_id: int, time_range=None) -> list[dict]:
    """ Calculates total and net profit for each product,
    the number of sales and the total number of items sold for the period=time_range.
    Enters data into a dictionary of the desired type.

    :param user_id: user.pk by which sales are filtered
    :param time_range: time range for which you need to select sales. Default time_range for today
    :return: tuple[list[dict], list[float], list[dict], list[dict]]
    """
    if time_range is None:
        time_range = [datetime.today(), datetime.today()]

    query_set = (
        Sale.objects.filter(user_id=user_id,
                            created_at__date__gte=time_range[0], created_at__date__lte=time_range[1])
        .select_related('product')
        .order_by('-quantity')
    )

    data_set = {}

    for sale in query_set:
        if sale.product_id not in data_set:
            data_set[sale.product_id] = {'product__name': sale.get_product_name,
                                         'total_score': round(sale.get_total_score, 2),
                                         'total_score_cleaned': round(sale.get_clean_total_score, 2),
                                         'total_quantity': 1,
                                         'total_quantity_all': sale.quantity
                                         }
        else:
            data_set[sale.product_id]['total_quantity'] += 1
            data_set[sale.product_id]['total_quantity_all'] += sale.quantity
            data_set[sale.product_id]['total_score'] += round(sale.get_total_score, 2)
            data_set[sale.product_id]['total_score_cleaned'] += round(sale.get_clean_total_score, 2)

    return list(data_set.values())


def get_total_profit_and_tax(data_set: list[dict]) -> list[float]:
    """
    Based on the passed list of dictionaries,
    calculates the total profit from
    the total cleaned profit and the total tax from all sales.

    Dictionaries must have keys 'total_score' and 'total_score_cleaned'.

    :param data_set: list[dict]
    :return: tuple(float)
    :raises KeyError
    """
    total_tax, total_profit, total_cleaned_profit = 0, 0, 0
    for sale in data_set:
        total_profit += sale['total_score']
        total_cleaned_profit += sale['total_score_cleaned']

    total_tax = total_profit * 0.06

    return [total_profit, total_cleaned_profit, total_tax]


def get_top_products(data_set: list[dict]) -> list[[dict]]:
    """
    The function takes a list of dictionaries. Based on it, 2 lists are formed: top_sales, top_profit.

    Dictionaries must have keys 'total_quantity_all' and 'total_score_cleaned'.
    End values are sorted in descending order

    :param data_set:
    :return: list with 2 float-values. top 5 products by the numbser of sales
    and top 5 products by cleaned profit for the period.
    :raises KeyError
    """
    top_sales = sorted(data_set, key=lambda sale: sale['total_quantity_all'], reverse=True)[:5]
    top_profit = sorted(data_set, key=lambda sale: sale['total_score_cleaned'], reverse=True)[:5]

    return [top_sales, top_profit]

