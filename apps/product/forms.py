from django import forms

from .models import Product


class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label='Price', widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_stock = forms.BooleanField(label='In Stock: ',
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'price', 'in_stock')


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
