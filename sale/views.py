from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class SaleListView(ListView):
    model = models.Sale
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


class SaleCreateView(CreateView):
    form_class = forms.SaleCreateForm
    model = models.Sale
    template_name = 'sale/create.html'

    def get_form_kwargs(self):
        """Update kwargs for hand over current-user object to form"""
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user_info': self.request.user if self.request.user.is_authenticated else None,
        })
        return kwargs


class SaleUpdateView(UpdateView):
    form_class = forms.SaleUpdateForm
    model = models.Sale
    template_name = 'sale/update.html'


class SaleDeleteView(DeleteView):
    model = models.Sale
    success_url = reverse_lazy('sales')
    template_name = 'sale/detail.html'


class RegisterUser(CreateView):
    form_class = forms.SignUpForm
    template_name = 'sale/registration.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'SignUp'}


class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'sale/login.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        return reverse_lazy('sales')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('login')
    template_name = 'sale/login.html'
