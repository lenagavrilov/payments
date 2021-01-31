from django import forms

class SearchForm(forms.Form):
    paymentKind = forms.CharField(label='From Payment Kind, max_length=2')

class AddPaymentKindForm(forms.Form):
    paymentKindCode = forms.IntegerField(label="Enter the code")
    definition = forms.CharField(label="Enter payment Kind", max_length=100)
    