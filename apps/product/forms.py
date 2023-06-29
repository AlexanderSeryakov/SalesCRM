from django import forms
from django.core.exceptions import ValidationError

from .models import Product
from .validators import max_length_name, try_to_get_price, validate_price


class ProductCreateForm(forms.ModelForm):
    """
    Form for create a new Product-object.
    Save-method override to automatically write current user to user-field.
    This form used in ProductCreateView.
    """

    def __init__(self, user_info, *args, **kwargs):
        self.user_info = user_info
        super().__init__(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.instance.user = self.user_info
        return super().save(*args, **kwargs)

    def clean_name(self):
        name = max_length_name(self.cleaned_data['name'])

        if Product.objects.filter(user=self.user_info, name=name):
            raise ValidationError(f'У вас уже есть товар с наименованием {name}')

        return name

    def clean_purchase_price(self):
        return validate_price(self.cleaned_data['purchase_price'])

    def clean_retail_price(self):
        retail_price = try_to_get_price(self.cleaned_data, key='retail_price')
        purchase_price = try_to_get_price(self.cleaned_data, key='purchase_price')
        if retail_price <= purchase_price:
            raise ValidationError('Розничная стоимость не может быть меньше закупочной.')
        return validate_price(retail_price)


class ProductUpdateForm(ProductCreateForm):
    def clean_name(self):
        name = max_length_name(self.cleaned_data['name'])

        if self.__dict__['initial']['name'] != name and \
                len(Product.objects.filter(user=self.__dict__['user_info'], name=name)):
            raise ValidationError(f'У вас уже есть товар с наименованием {name}')

        return name
