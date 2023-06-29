from datetime import datetime

from django.shortcuts import redirect, render
from django.views import View

from .forms import MyDateInput
from .utils import (get_top_products, get_total_profit_and_tax,
                    get_valid_data_for_template)


class AnalyticsView(View):
    template = 'analytics/base.html'
    date_form = MyDateInput()
    title = 'Аналитика'

    def get(self, request):
        data_set = get_valid_data_for_template(self.request.user.pk)
        total_values = get_total_profit_and_tax(data_set)
        top_sales, top_profit = get_top_products(data_set)

        time_range = datetime.today()

        return render(request, template_name=self.template, context={'data_set': data_set, 'form': self.date_form,
                                                                     'title': self.title,
                                                                     'time_start': time_range,
                                                                     'time_end': time_range,
                                                                     'total_values': total_values,
                                                                     'top_sales': top_sales,
                                                                     'top_profit': top_profit,
                                                                     })

    def post(self, request):
        try:
            time_range = [request.POST['start_date'], request.POST['end_date']]
        except KeyError:
            return redirect('analytics')

        data_set = get_valid_data_for_template(self.request.user.pk, time_range=time_range)
        total_values = get_total_profit_and_tax(data_set)
        top_sales, top_profit = get_top_products(data_set)

        time_for_template = [datetime.strptime(time_range[0], '%Y-%m-%d'), datetime.strptime(time_range[1], '%Y-%m-%d')]

        return render(request, template_name=self.template, context={'data_set': data_set, 'form': self.date_form,
                                                                     'title': self.title,
                                                                     'time_start': time_for_template[0],
                                                                     'time_end': time_for_template[1],
                                                                     'total_values': total_values,
                                                                     'top_sales': top_sales,
                                                                     'top_profit': top_profit,
                                                                     })

