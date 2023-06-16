from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.product.models import Product


class CurrentUserMixin:
    """ Mixin for hand-over current user and append user-object in kwargs.
        Use it in child-class of CreateView only!
     """
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user_info': self.request.user if self.request.user.is_authenticated else None,
        })
        return kwargs


class UserProductsMixin:
    """
    Mixin to get the products of the current user.
    Adds a new 'product' ModelChoiceField field to the form or overrides
    a hidden 'product' field.
    Use it with CreateView, UpdateView inheritors.
    """
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        form.fields['product'] = forms.ModelChoiceField(label='Product',
                                                        queryset=Product.objects.filter(user_id=self.request.user.pk,
                                                                                        in_stock=True),
                                                        widget=forms.Select(attrs={'class': 'form-select'}))
        return form


class CustomLoginRequiredMixin(LoginRequiredMixin, ):
    """
    Mixin for checking user is logged in.
    If user is AnonymousUser - redirect to login page.

    You can use it in anything CBV.
    """
    login_url = '/auth/login/'
    redirect_field_name = None
