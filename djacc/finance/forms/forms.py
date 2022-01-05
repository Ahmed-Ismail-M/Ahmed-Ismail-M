from django import forms

class NewTransferForm(forms.Form):
    amount = forms.DecimalField(label="Amount", min_value=1)
    