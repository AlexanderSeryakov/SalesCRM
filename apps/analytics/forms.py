from django import forms


class MyDateInput(forms.Form):
    start_date = forms.DateField(label='С :',
                                 widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), required=True)
    end_date = forms.DateField(label='По :',
                               widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), required=True)
