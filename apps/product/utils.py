from apps.sale.models import Sale


def calculate_product_values(context):
    """
    Function calculating total number of product sold,
    num of sales, total cleaned profit of current product
    and adds this values to context.

    :param context:
    :return: context
    """
    curr_product = context['product']
    sales = Sale.objects.filter(user_id=curr_product.user_id, product_id=curr_product.id).select_related('product')
    total = 0
    for sale in sales:
        total += sale.quantity
    context['total_quantity'] = total
    context['sales_count'] = sales.count()
    context['cleaned_profit'] = round(context['product'].retail_price * 0.94 - context['product'].purchase_price, 2)

    return context

