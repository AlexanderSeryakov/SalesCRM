import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Sale
from .validators import validate_phone_number


class SaleCreateForm(forms.ModelForm):
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
        if 0 < quantity < 101:
            return quantity
        raise ValidationError('Количество не может превышать 100 единиц и не может быть меньше 1.')

    def clean_discount(self):
        discount = self.cleaned_data['discount']
        if discount == '':
            raise ValidationError('Скидка не может быть пустым полем. Если скидка не была предоставлена '
                                  '- поставьте значение 0')
        if discount.count('%') > 1 or any(map(lambda sign: sign in discount, '-,./!@`~=\\|/?#$№;:*][}{)(<>')):
            raise ValidationError('Укажите корректный формат скидки')
        elif '%' in discount:
            d = re.findall('\d+%', discount)
            if len(d[0].replace('%', '')) > 2:
                raise ValidationError('Укажите корректный формат скидки')
        return discount

    def clean_customer_phone(self):
        return validate_phone_number(self.cleaned_data['customer_phone'])


class SaleUpdateForm(SaleCreateForm):
    """ Form for update sale-object.
        This for used in SaleUpdateView.

        You can customize this class of override some methods if you needed.
    """

