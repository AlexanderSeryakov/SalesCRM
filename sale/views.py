from django.views.generic import TemplateView, ListView
from . import models


class SalesPageView(ListView):
    model = models.Sale
    http_method_names = ['get', 'head']
    template_name = 'sale/sales.html'
    context_object_name = 'sales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sales'
        return context
