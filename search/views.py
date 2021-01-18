from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Payments, Supplyer

columnsNames = ["Payment", "Check Number", "Payment Date", "Supplyer", "Details", "Given On", "Payment number ...", "Out of...", "Status", 
                "Refuse Reason", "Refuse Date", "Given Instead", "Alternative Supplier", "Checkbook"]

columnsValues = [10,2,3,4,5,6,7,8,9,10,11,12,13,14]

class AddPaymentForm(forms.Form):
    paymentKind = forms.CharField(label='Payment Kind')
    

# Create your views here.
def index(request):
    return render(request, 'search/index.html', {
        "columnsNames": columnsNames,
        "columnsValues": columnsValues,
        "payments": Payments.objects.all(),
        "supplyers": Supplyer.objects.all()
    })

def addpayment(request):
    if request.method == "POST":
      form = AddPaymentForm(request.POST)
      if form.is_valid():
        colName = form.cleaned_data["paymentKind"]
        columnsNames.append(colName)
        return HttpResponseRedirect(reverse("search:index"))
      else:
        return render(request, "search/addpayment.html", {
            "form": form
        })

    return render(request, "search/addpayment.html", {
       "form": AddPaymentForm()
        })

def payment(request, payment_id):
    payment = Payments.objects.get(pk=payment_id)
    return render(request, "search/payment.html", {
        "payment": payment
    })
    