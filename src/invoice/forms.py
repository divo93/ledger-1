from django import forms
from src.invoice.models import CustomerModel, BillModel


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = (
            'c_name',
            'mob',
        )


class BillForm(forms.ModelForm):
    class Meta:
        model = BillModel
        fields = (
            'mode_of_payment',
            'other_payment_option'
            'Shop_details'
        )
