from django import forms


class AddNewProductCart(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=15, step_size=1, widget=forms.NumberInput(attrs={'class':'button__counter-number',
                                                                                                          'disabled': 'disabled'}), initial=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput())

