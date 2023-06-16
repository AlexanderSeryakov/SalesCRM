from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from apps.common_utils import CurrentUserMixin, UserProductsMixin, CustomLoginRequiredMixin

from .forms import SaleCreateForm, SaleUpdateForm
from .models import Sale
from .utils import SaleModelMixin


class SaleListView(CustomLoginRequiredMixin, ListView):
    template_name = 'sale/sales.html'
    context_object_name = 'sales'
    extra_context = {'title': 'Sales'}

    def get_queryset(self):
        return Sale.objects.filter(user_id=self.request.user.pk).select_related('product')


class SaleDetailView(CustomLoginRequiredMixin, SaleModelMixin, DetailView):
    template_name = 'sale/detail.html'
    context_object_name = 'detail'
    extra_context = {'title': 'Edit Sale'}


class SaleCreateView(CustomLoginRequiredMixin, SaleModelMixin, CurrentUserMixin, UserProductsMixin, CreateView):
    form_class = SaleCreateForm
    template_name = 'sale/create.html'
    extra_context = {'title': 'New Sale'}


class SaleUpdateView(CustomLoginRequiredMixin, SaleModelMixin, UserProductsMixin, UpdateView):
    form_class = SaleUpdateForm
    template_name = 'sale/update.html'
    extra_context = {'title': 'Edit'}


class SaleDeleteView(CustomLoginRequiredMixin, SaleModelMixin, DeleteView):
    template_name = 'sale/detail.html'
    success_url = reverse_lazy('sales')
