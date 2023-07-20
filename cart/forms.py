from django import forms

from cart.models import Promotions


class AddNewProductCart(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=15, step_size=1, widget=forms.NumberInput(attrs={'class':'button__counter-number', 'id':"quantity-input", 'name': "quantity"}), initial=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput())


class UsePromotion(forms.ModelForm):
    class Meta:
        model = Promotions
        fields = ['promocode']

        widgets = {
            'promocode': forms.TextInput(attrs={'class': 'busket-result__input','placeholder': 'Введите промокод'}),
        }
