from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import LoginUserForm, SignUpForm, SaleUpdateForm, SaleCreateForm, TestForm
from .models import Sale
from .utils import SaleModelMixin
# from . import forms, models
from apps.common_utils import CurrentUserMixin
from apps.product.models import Product


class TestView(View):
    def get(self, request, *args, **kwargs):
        initial = {}
        q = Product.objects.filter(user_id=request.user.pk, in_stock=True)
        choices = [(p.pk, p.name) for p in q]
        print(choices)
        choice_field = forms.ChoiceField(label='Choices', choices=choices)
        form_class = TestForm
        form = form_class(initial=initial)
        form.fields['resp'] = choice_field
        print(form)
        return render(request, 'common/test.html', context={'choices': choices, 'form': form})


class SaleListView(ListView):
    template_name = 'sale/sales.html'
    context_object_name = 'sales'
    extra_context = {'title': 'Sales'}

    def get_queryset(self):
        return Sale.objects.filter(user_id=self.request.user.pk).select_related('product')


class SaleDetailView(SaleModelMixin, DetailView):
    template_name = 'sale/detail.html'
    context_object_name = 'detail'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Detail: {self.request.__dict__['resolver_match'].kwargs['pk']}"
        return context


class SaleCreateView(SaleModelMixin, CurrentUserMixin, CreateView):
    form_class = SaleCreateForm
    template_name = 'sale/create.html'
    extra_context = {'title': 'New Sale'}


class SaleUpdateView(SaleModelMixin, UpdateView):
    form_class = SaleUpdateForm
    template_name = 'sale/update.html'
    extra_context = {'title': 'Edit'}


class SaleDeleteView(SaleModelMixin, DeleteView):
    template_name = 'sale/detail.html'
    success_url = reverse_lazy('sales')


class RegisterUserView(CreateView):
    form_class = SignUpForm
    template_name = 'sale/registration.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'SignUp'}


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'sale/login.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        return reverse_lazy('sales')


class LogoutUserView(LogoutView):
    template_name = 'sale/login.html'
    next_page = reverse_lazy('login')
