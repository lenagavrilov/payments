from django import forms
from django.forms import ModelForm
from . models import PaymentsKind, Payments


class SearchForm(forms.Form):
    paymentKind = forms.CharField(label='From Payment Kind, max_length=2')

#class AddPaymentKindForm(forms.Form):
 #   definition = forms.ModelChoiceField(queryset=PaymentsKind.objects.all(),
  #                                      label="Enter new payment kind")

class AddPaymentKindForm(forms.Form):
   # codePaymentKind = forms.ModelChoiceField(queryset=PaymentsKind.objects.all())
    definition = forms.CharField(label="Enter new PaymentKind", max_length=50)



