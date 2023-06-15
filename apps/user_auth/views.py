from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.user_auth.forms import LoginUserForm, SignUpForm


class RegisterUserView(CreateView):
    form_class = SignUpForm
    template_name = 'user_auth/registration.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'SignUp'}


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'user_auth/login.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        return reverse_lazy('sales')


class LogoutUserView(LogoutView):
    template_name = 'user_auth/login.html'
    next_page = reverse_lazy('login')
