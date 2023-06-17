from datetime import datetime

from django.db.models import Sum, F, Count
from django.shortcuts import render

from apps.sale.models import Sale


def home(request):
    """<QuerySet [{'product__name': 'Window', 'total_quantity': 1, 'total_sum': 84000.0, 'total_sum_with_discount':
    83160.0}, ...]>
    """
    # , created_at__date=time_now
    time_now = datetime.today()
    data_set = (
        Sale.objects.filter(user_id=request.user.pk, created_at__date=time_now)
        .select_related('product')
        .values('product__name')
        .annotate(total_quantity=Count(F('product_id')),
                  total_sum=Sum(F('product__price') * F('quantity')),
                  total_sum_with_discount=Sum(F('product__price') * F('quantity') * (1 - F('discount') / 100)))
        .order_by('-total_sum'))

    # print(data_set)
    return render(request, 'analytics/gcharts.html', {'data_set': data_set, 'title': 'Statistic', 'today': time_now})
