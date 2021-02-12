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
        fromPaymentKind = request.POST['frompaymentKind']
        toPaymentKind = request.POST["topaymentKind"]
        fromPaymentDate = request.POST['paymentfromDate']
        toPaymentDate = request.POST['paymentToDate']
        fromSupplyer = request.POST['fromSupplyer']
        toSupplyer = request.POST['toSupplyer']
        fromStatus = request.POST['fromStatus']
        toStatus = request.POST['toStatus']
        payments_filter= {'paymentDate__gte' : fromPaymentDate, 
            'paymentDate__lte' : toPaymentDate,
            'paymentKind__gte' : fromPaymentKind,
            'paymentKind__lte' : toPaymentKind,
            'supplyer__gte' : fromSupplyer,
            'supplyer__lte' : toSupplyer,
            'status__gte' : fromStatus,
            'status__lte' : toStatus}
        return render(request, 'search/index.html', {
        "columnsNames": columnsNames,
        "payments": Payments.objects.filter(**payments_filter),
        "supplyers": Supplyer.objects.all(),
        "fromSupplyers": Supplyer.objects.filter,
        "toSupplyers": toSupplyer,
        "paymentKinds": PaymentsKind.objects.all(),
        "checks": Payments.objects.filter(checkNumber__isnull=False),
        "statuses": Status.objects.all(),
        "startDate": fromPaymentDate,
        "finishDate": toPaymentDate,
        
        "total": Payments.objects.filter(**payments_filter).aggregate(Sum('amount')),
        "totalCount": Payments.objects.filter(**payments_filter).aggregate(Count('amount'))
                    })

    return render(request, 'search/index.html', {
        "columnsNames": columnsNames,
        "payments": Payments.objects.filter(
            paymentDate__gte = startDate(), 
            paymentDate__lte = finishDate(),
        ),
        "supplyers": Supplyer.objects.all(),
     #   "fromSupplyers": Supplyer.objects.all(),
     #   "toSupplyers": Supplyer.objects.all(),
        "paymentKinds": PaymentsKind.objects.all(),
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
       
           paymentDefinition = form.cleaned_data["definition"]
           newPaymentKind = PaymentsKind(definition=paymentDefinition)
           newPaymentKind.save()
           return HttpResponseRedirect(reverse('search:addpaymentkind'))
       else:
           form=AddPaymentKindForm()
    
    return render (request, "search/addpaymentkind.html", {
        "form": AddPaymentKindForm(),
        "paymentKinds": PaymentsKind.objects.all()
    
    })

