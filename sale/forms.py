from typing import Any

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Sale


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'jojoe@gmail.com'}))
    first_name = forms.CharField(label='', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Jonathan'}))
    last_name = forms.CharField(label='', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Joestar'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # override default widget attrs to custom
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted "><small>Required. 150 characters or fewer. ' \
                                    'Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar ' \
                                     'to your other personal information.</li><li>Your password must contain at least' \
                                     ' 8 characters.</li><li>Your password can\'t be a commonly used password.' \
                                     '</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, ' \
                                     'for verification.</small></span>'


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SaleUpdateForm(forms.ModelForm):
    """ Form for update sale-object.
        This for used in SaleUpdateView.
    """
    product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class': 'form-control'}))
    discount = forms.IntegerField(label='Discount', widget=forms.TextInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Sale
        fields = ('product_name', 'customer_name', 'price', 'discount', 'notes')


class SaleCreateForm(SaleUpdateForm):
    """
        Form for create a new Sale-object.
        Save-method override to automatically write current user to user-field.
        This form used in SaleCreateView.
    """
    def __init__(self, user_info, *args, **kwargs):
        self.user_info = user_info
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user_info
        return super().save(*args, **kwargs)

