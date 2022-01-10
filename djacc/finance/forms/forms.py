from django import forms

class NewTransferForm(forms.Form):
    amount = forms.DecimalField(label="Amount",min_value=1)
    cust_name = forms.ChoiceField(label="Customer", choices=[("0","")])
    def __init__(self,choices, max_value, *args, **kwargs):
        super(NewTransferForm, self).__init__(*args, **kwargs)
        self.fields['cust_name'].choices = choices
        self.fields['amount'] = forms.DecimalField(max_value= max_value, min_value=1)