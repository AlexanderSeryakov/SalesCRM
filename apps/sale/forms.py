from django import forms
from .models import Sale


class SaleUpdateForm(forms.ModelForm):
    """ Form for update sale-object.
        This for used in SaleUpdateView.
    """
    product = forms.HiddenInput()
    customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_phone = forms.CharField(label='Customer phone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='Quantity', widget=forms.TextInput(attrs={'class': 'form-control'}))
    discount = forms.IntegerField(label='Discount', widget=forms.TextInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(label='Comments', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = Sale
        fields = ('product', 'customer_name', 'customer_phone', 'quantity', 'discount', 'notes')


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
