from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import models, forms


class SalesPageView(ListView):
    model = models.Sale
    # http_method_names = ['get', 'head']
    template_name = 'sale/sales.html'
    context_object_name = 'sales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sales'
        return context

    def get_queryset(self):
        return models.Sale.objects.filter(user_id=self.request.user.pk)


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
