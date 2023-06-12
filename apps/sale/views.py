from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from . import forms, models
from apps.common_utils import CurrentUserMixin


class SaleListView(ListView):
    template_name = 'sale/sales.html'
    context_object_name = 'sales'
    extra_context = {'title': 'Sales'}

    def get_queryset(self):
        return models.Sale.objects.filter(user_id=self.request.user.pk)


class SaleDetailView(DetailView):
    model = models.Sale
    template_name = 'sale/detail.html'
    context_object_name = 'detail'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Detail: {self.request.__dict__['resolver_match'].kwargs['pk']}"
        return context


class SaleCreateView(CurrentUserMixin, CreateView):
    form_class = forms.SaleCreateForm
    model = models.Sale
    template_name = 'sale/create.html'
    extra_context = {'title': 'New Sale'}


class SaleUpdateView(UpdateView):
    form_class = forms.SaleUpdateForm
    model = models.Sale
    template_name = 'sale/update.html'
    extra_context = {'title': 'Edit'}


class SaleDeleteView(DeleteView):
    model = models.Sale
    success_url = reverse_lazy('sales')
    template_name = 'sale/detail.html'


class ProductListView(ListView):
    model = models.Product


class RegisterUserView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'sale/registration.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'SignUp'}


class LoginUserView(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'sale/login.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        return reverse_lazy('sales')


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('login')
    template_name = 'sale/login.html'
