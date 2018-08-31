from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    email = forms.EmailField(required=False)
    address = forms.CharField(max_length=250, label='Адресс доставки')

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number', 'email')
        labels = {
            'first_name': ('Имя'),
            'last_name': ('Фамилия'),
            'phone_number': ('Номер телефона'),
            'email': 'мыло'
            }
