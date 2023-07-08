from django.http import Http404
from django.shortcuts import render
from apps.product.models import Product
from django.views.generic import ListView, DetailView
from apps.common_mixins import CustomLoginRequiredMixin
from django.urls import reverse
from .models import Supply


class SupplyListView(CustomLoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = 'supply/supplies.html'
    extra_context = {'title': 'Поставки'}
    context_object_name = 'supplies'

    def get_queryset(self):
        return Supply.objects.filter(user_id=self.request.user.pk)


class SupplyDetailView(CustomLoginRequiredMixin, DetailView):
    template_name = 'supply/supply_detail.html'
    extra_context = {'title': 'О поставке'}
    context_object_name = 'supply'

    def get_object(self, queryset=None):
        supply_id = self.kwargs.get(self.pk_url_kwarg)

        if not queryset:
            queryset = Supply.objects.filter(user_id=self.request.user.pk).select_related('user')

        if supply_id:
            queryset = queryset.filter(pk=supply_id)
        
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                ('Error. Please, enter correct ID!')
            )
        return obj
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # products = prepare_products_list_to_template(self.get_object().products)
    #     context['products'] = self.get_object().products

    #     return context



def add_new_supply(request):
    products = Product.objects.filter(user_id=request.user.pk)
    if request.user.is_authenticated:
        return render(request, 'supply/create_supply.html', {'title': 'Новая поставка', 'products': products})
    
    return reverse('login')

