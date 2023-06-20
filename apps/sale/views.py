from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from apps.common_utils import (CurrentUserMixin, CustomLoginRequiredMixin,
                               UserProductsMixin)

from .forms import SaleCreateForm, SaleUpdateForm
from .models import Sale
from .utils import UserSalePermissionMixin


class SaleListView(CustomLoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = 'sale/sales.html'
    context_object_name = 'sales'
    extra_context = {'title': 'Sales'}

    def get_queryset(self):
        return Sale.objects.filter(user_id=self.request.user.pk).select_related('product')


class SaleDetailView(CustomLoginRequiredMixin, UserSalePermissionMixin, DetailView):
    model = Sale
    template_name = 'sale/detail.html'
    context_object_name = 'detail'
    extra_context = {'title': 'Edit Sale'}


class SaleCreateView(CustomLoginRequiredMixin, CurrentUserMixin, UserProductsMixin, CreateView):
    model = Sale
    form_class = SaleCreateForm
    template_name = 'sale/create.html'
    extra_context = {'title': 'New Sale'}


class SaleUpdateView(CustomLoginRequiredMixin, UserProductsMixin, UserSalePermissionMixin, UpdateView):
    model = Sale
    form_class = SaleUpdateForm
    template_name = 'sale/update.html'
    extra_context = {'title': 'Edit'}


class SaleDeleteView(CustomLoginRequiredMixin, UserSalePermissionMixin, DeleteView):
    model = Sale
    template_name = 'sale/detail.html'
    success_url = reverse_lazy('sales')
