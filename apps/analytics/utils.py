from datetime import datetime

from apps.sale.models import Sale


def get_valid_data_for_template(user_id, time_range=None):
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
            data_set[sale.product_id] = {'product__name': sale.get_product_name, 'total_score': sale.get_total_score,
                                         'total_score_cleaned': sale.get_clean_total_score, 'total_quantity': 1,
                                         'total_quantity_all': sale.quantity
                                         }
        else:
            data_set[sale.product_id]['total_quantity'] += 1
            data_set[sale.product_id]['total_quantity_all'] += sale.quantity
            data_set[sale.product_id]['total_score'] += sale.get_total_score
            data_set[sale.product_id]['total_score_cleaned'] += sale.get_clean_total_score

    return list(data_set.values())

