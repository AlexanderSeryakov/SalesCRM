from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from . import models, forms


class SaleListView(ListView):
    model = models.Sale
    template_name = 'sale/sales.html'
    context_object_name = 'sales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sales'
        return context

    def get_queryset(self):
        return models.Sale.objects.filter(user_id=self.request.user.pk)


class SaleDetailView(DetailView):
    model = models.Sale
    template_name = 'sale/detail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"detail {self.request.__dict__['resolver_match'].kwargs['pk']}"
        return context


class SaleCreateView(CreateView):
    model = models.Sale


class SaleDeleteView(DeleteView):
    model = models.Sale


class RegisterUser(CreateView):
    form_class = forms.SignUpForm
    template_name = 'sale/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SignUp'
        return context


class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'sale/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('sales')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('login')
    template_name = 'sale/login.html'

