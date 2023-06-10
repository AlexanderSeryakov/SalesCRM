from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .utils import ProductModelMixin


class ProductListView(ProductModelMixin, ListView):
    context_object_name = 'products'
    extra_context = {'title': 'Products'}
    template_name = 'product/products.html'


class ProductDetailView(ProductModelMixin, DetailView):
    context_object_name = 'product'
    extra_context = {'title': 'Product'}
    template_name = 'product/detail.html'


class ProductCreateView(ProductModelMixin, CreateView):
    template_name = 'product/create.html'
    extra_context = {'title': 'New Product'}
    fields = ('name', 'price')

