from django import forms

from .models import Product


class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Наименование', widget=forms.TextInput(attrs={'class': 'form-control'}))
    purchase_price = forms.DecimalField(label='Закупочная стоимость',
                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    retail_price = forms.DecimalField(label='Розничная стоимость',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_stock = forms.BooleanField(label='В наличии: ',
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check'}), required=False)
    notes = forms.CharField(label='Доп.заметки', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = Product
        fields = ('name', 'purchase_price', 'retail_price', 'in_stock', 'notes')


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
