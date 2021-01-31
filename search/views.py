from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Payments, Supplyer, PaymentsKind, Status
from django.db.models import Sum, Max, Count

from . forms import AddPaymentKindForm



import datetime
import calendar

columnsNames = ["Payment", "Amount", "Check Number", "Payment Date", "Supplyer", "Details", "Given On", "Payment number ...", "Out of...", "Status", 
                "Refuse Reason", "Refuse Date", "Given Instead", "Alternative Supplier", "Checkbook"]


class AddPaymentForm(forms.Form):
    paymentKind = forms.CharField(label='Payment')




def startDate():
    todaysdate = datetime.date.today()
    startMonth = datetime.datetime(todaysdate.year, todaysdate.month, 1)
    startMonth = startMonth.strftime("%Y-%m-%d") 
    return startMonth

def finishDate():
    todaysdate =  datetime.date.today()
    daysInMonth = calendar.monthrange(todaysdate.year, todaysdate.month)[1]
    finishMonth = datetime.datetime(todaysdate.year, todaysdate.month, daysInMonth)
    finishMonth = finishMonth.strftime("%Y-%m-%d") 
    return finishMonth
 

# Create your views here.
def index(request):
    if request.method == "POST":
        return HttpResponse('hi')
    else:
        return render(request, 'search/index.html', {
        "columnsNames": columnsNames,
        "payments": Payments.objects.filter(paymentDate__gte = startDate(), paymentDate__lte = finishDate()),
     #  "payments": Payments.objects.all(),
        "supplyers": Supplyer.objects.all(),
        "paymentKinds": PaymentsKind.objects.all(),
       # "maxPaymentKind": PaymentsKind.objects.aggregate(Max('paymentKindCode')),
        "checks": Payments.objects.filter(checkNumber__isnull=False),
        "statuses": Status.objects.all(),
        "startDate": startDate(),
        "finishDate": finishDate(),
        "total": Payments.objects.filter(paymentDate__gte = startDate(), paymentDate__lte = finishDate()).aggregate(Sum('amount')),
        "totalCount": Payments.objects.filter(paymentDate__gte = startDate(), paymentDate__lte = finishDate()).aggregate(Count('amount'))
        
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

def addpaymentkind(request):
    if request.method == "POST":
       form = AddPaymentKindForm(request.POST)
        
       if form.is_valid():
           paymentKindCode = form.cleaned_data["paymentKindCode"]
           paymentDefinition = form.cleaned_data["definition"]
           newRow = PaymentsKind(paymentKindCode=paymentKindCode,
                                definition=paymentDefinition)
           newRow.save()
           return HttpResponseRedirect(reverse('search:addpaymentkind'))
       else:
           form=AddPaymentKindForm()
    
    return render (request, "search/addpaymentkind.html", {
        "form": AddPaymentKindForm(),
        "paymentKinds": PaymentsKind.objects.all()
    
    })

