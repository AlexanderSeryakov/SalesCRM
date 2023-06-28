from django import forms
from django.core.exceptions import ValidationError

from .models import Product
from .validators import is_positive_price, is_correct_price


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'purchase_price', 'retail_price', 'in_stock', 'notes')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_price': forms.TextInput(attrs={'class': 'form-control'}),
            'retail_price': forms.TextInput(attrs={'class': 'form-control'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 20:
            raise ValidationError('Наименование товара не должно превышать 20 символов.')
        return name

    def clean_purchase_price(self):
        return is_positive_price(self.cleaned_data['purchase_price'])

    def clean_retail_price(self):
        retail_price = is_correct_price(self.cleaned_data, key='retail_price')
        purchase_price = is_correct_price(self.cleaned_data, key='purchase_price')
        if retail_price <= purchase_price:
            raise ValidationError('Розничная стоимость не может быть меньше закупочной.')
        return is_positive_price(retail_price)


class ProductCreateForm(ProductUpdateForm):
    """
        Form for create a new Product-object.
        Save-method override to automatically write current user to user-field.
        This form used in ProductCreateView.
    """

    def __init__(self, user_info, *args, **kwargs):
        self.user_info = user_info
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user_info
        return super().save(*args, **kwargs)
