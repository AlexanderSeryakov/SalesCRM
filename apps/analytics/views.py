from datetime import datetime

from django.db.models import Sum, F, Count
from django.shortcuts import render, redirect

from apps.sale.models import Sale
from .forms import MyDateInput


def home(request, time_range=None):
    """<QuerySet [{'product__name': 'Window', 'total_quantity': 1, 'total_sum': 84000.0, 'total_sum_with_discount':
    83160.0}, ...]>
    """
    if time_range is None:
        time_range = [datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%Y-%m-%d')]

    date_form = MyDateInput()
    data_set = (
        Sale.objects.filter(user_id=request.user.pk,
                            created_at__date__gte=time_range[0], created_at__date__lte=time_range[1])
        .select_related('product')
        .values('product__name')
        .annotate(total_quantity=Count(F('product__name')),
                  total_quantity_all=Sum(F('quantity')),
                  total_sum=Sum(F('product__price') * F('quantity')),
                  total_sum_with_discount=Sum(F('product__price') * F('quantity') * (1 - F('discount') / 100)))
        .order_by('-total_quantity')
    )

    return render(request, 'analytics/base.html', {'data_set': data_set, 'title': 'Statistic',
                                                   'time_start': datetime.strptime(time_range[0], '%Y-%m-%d'),
                                                   'time_end': datetime.strptime(time_range[1], '%Y-%m-%d'),
                                                   'form': date_form})


def view_period(request):

    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    return home(request, time_range=[start_date, end_date])
