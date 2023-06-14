from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from apps.common_utils import CurrentUserMixin
from apps.sale.models import Sale

from .forms import ProductCreateForm, ProductUpdateForm
from .models import Product
from .utils import ProductModelMixin, UserProductPermissionMixin


class ProductListView(ProductModelMixin, ListView):
    context_object_name = 'products'
    extra_context = {'title': 'Products'}
    template_name = 'product/products.html'

    def get_queryset(self):
        return Product.objects.filter(user_id=self.request.user.pk)


class ProductDetailView(ProductModelMixin, UserProductPermissionMixin, DetailView):
    context_object_name = 'product'
    extra_context = {'title': 'Product'}
    template_name = 'product/detail.html'


class ProductCreateView(ProductModelMixin, CurrentUserMixin, CreateView):
    form_class = ProductCreateForm
    template_name = 'product/create.html'
    extra_context = {'title': 'New Product'}


class ProductUpdateView(ProductModelMixin, UserProductPermissionMixin, UpdateView):
    form_class = ProductUpdateForm
    template_name = 'product/update.html'
    extra_context = {'title': 'Edit Product'}


class ProductDeleteView(ProductModelMixin, UserProductPermissionMixin, DeleteView):
    success_url = reverse_lazy('product')
    template_name = 'product/products.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        if Sale.objects.filter(product_id=self.object.id):
            messages.error(self.request, 'С этим товаром связаны продажи, удаление невозможно! '
                                         'Если товар отсутствует, установите флаг in_stock в выключеное положение!')
            return HttpResponseRedirect(success_url)
        self.object.delete()
        messages.success(self.request, 'Товар успешно удалён!')
        return HttpResponseRedirect(success_url)
