import re
from django import forms
from django.core.exceptions import ValidationError

from .models import Sale


class SaleUpdateForm(forms.ModelForm):
    """ Form for update sale-object.
        This for used in SaleUpdateView.
    """
    product = forms.HiddenInput()

    class Meta:
        model = Sale
        fields = ('product', 'customer_phone', 'quantity', 'discount', 'notes')
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity > 0:
            return quantity
        raise ValidationError('Количество должно быть больше 0.')

    def clean_discount(self):
        discount = self.cleaned_data['discount']
        if discount.count('%') > 1 or any(map(lambda sign: sign in discount, '-,./!@`~=\\|/?#$№;:*][}{)(<>')):
            raise ValidationError('Укажите корректный формат скидки')
        elif '%' in discount:
            d = re.findall('\d+%', discount)
            if len(d[0].replace('%', '')) > 2:
                raise ValidationError('Укажите корректный формат скидки')
        return discount


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
