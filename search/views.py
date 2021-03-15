from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Payments, Supplyer, PaymentsKind, Status
from django.db.models import Sum, Max, Count
from django.db import IntegrityError
from django.contrib import messages
from . forms import AddPaymentKindForm

import logging

import datetime
import calendar

columnsNames = ["Payment", "Amount", "Check Number", "Payment Date", "Supplyer", "Details", "Given On", "Payment number ...", "Out of...", "Status", 
                "Refuse Reason", "Refuse Date", "Given Instead", "Alternative Supplier", "Checkbook"]


class AddPaymentForm(forms.Form):
    paymentKind = forms.CharField(label='Payment Kind')
    checkNumber = forms.IntegerField(label='Check Number')



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

 
def index(request):
    payments_filter = {}

    if request.method == "POST":
        
        
        status_list = request.POST.getlist('statuses')
        payments_filter['status' + '__in'] = status_list

        fromPaymentDate = request.POST['paymentfromDate']
        toPaymentDate = request.POST['paymentToDate']
        payments_filter['paymentDate__gte'] = fromPaymentDate
        payments_filter['paymentDate__lte'] = toPaymentDate


        all_payment_kinds = request.POST.get('all_payment_kinds')
        if all_payment_kinds:
            paymentKind = int(request.POST['frompaymentKind'])
            toPaymentKind = int(request.POST['topaymentKind'])
        else:
            paymentKind = int(request.POST['frompaymentKind'])
            toPaymentKind = paymentKind 
        payments_filter['paymentKind__gte'] = paymentKind
        payments_filter['paymentKind__lte'] = toPaymentKind


        all_checks = request.POST.get('all_checks')
        check_dates = request.POST.get('check_dates')
        if all_checks:
            from_check = int(request.POST['fromChecks'])
            to_checks = int(request.POST['toChecks'])
        else:
            from_check = int(request.POST['fromChecks'])
            to_checks = from_check 
        if not all_payment_kinds and paymentKind == 1:
            payments_filter['checkNumber__gte'] = from_check
            payments_filter['checkNumber__lte'] = to_checks
            if check_dates == 'all_dates':
                fromPaymentDate = '2000-01-01'
                payments_filter['paymentDate__gte'] = fromPaymentDate
                toPaymentDate = '2100-01-01'
                payments_filter['paymentDate__lte'] = toPaymentDate


        all_supplyers = request.POST.get('all_supplyers')
        if all_supplyers:
            fromSupplyer = int(request.POST['fromSupplyer']) 
            toSupplyer = int(request.POST["toSupplyer"])
        else:
            fromSupplyer = int(request.POST['fromSupplyer']) 
            toSupplyer = fromSupplyer
        payments_filter['supplyer__gte'] = fromSupplyer
        payments_filter['supplyer__lte'] = toSupplyer

        print(payments_filter)
        print(status_list)
    
        return render(request, 'search/index.html', {
                                "columnsNames": columnsNames,
                                "payments": Payments.objects.filter(**payments_filter),
                                "supplyers": Supplyer.objects.all(),
                                "fromSupplyers": Supplyer.objects.filter,
                                "toSupplyers": toSupplyer,
                                "paymentKinds": PaymentsKind.objects.order_by('id'),
                                "fromPaymentKind": paymentKind,
                                "toPaymentKind": toPaymentKind,
                                "checks": Payments.objects.filter(checkNumber__isnull=False).order_by('checkNumber'),
                                "statuses": Status.objects.all(),
                                "startDate": fromPaymentDate,
                                "finishDate": toPaymentDate,
                                "check_dates": check_dates,
                                "chosen_statuses": Status.objects.filter(statusCode__in = status_list),
                                "all_payment_kinds": all_payment_kinds,
                                "all_checks": all_payment_kinds,
                                "all_supplyers": all_supplyers,
                                "total": Payments.objects.filter(**payments_filter).aggregate(Sum('amount')),
                                "totalCount": Payments.objects.filter(**payments_filter).aggregate(Count('amount'))
                                            })
    
  
    status_list = Status.objects.all()
    payments_filter['status' + '__in'] = status_list
    payments_filter['paymentDate__gte'] = startDate()
    payments_filter['paymentDate__lte'] = finishDate() 
    print(status_list)                   
    print(payments_filter)
    return render(request, 'search/index.html', {
        "columnsNames": columnsNames,
        "payments": Payments.objects.filter(**payments_filter),

        "supplyers": Supplyer.objects.all(),
        "all_payment_kinds": 'on',
        "all_checks": 'on',
        "all_supplyers": 'on',
        "check_dates": 'all_dates',
        "paymentKinds": PaymentsKind.objects.order_by('id'),
        "checks": Payments.objects.filter(checkNumber__isnull=False).order_by('checkNumber'),
        "statuses": Status.objects.all(),
        "startDate": startDate(),
        "finishDate": finishDate(),
        "chosen_statuses": status_list,
        "total": Payments.objects.filter(paymentDate__gte = startDate(), paymentDate__lte = finishDate()).aggregate(Sum('amount')),
        "totalCount": Payments.objects.filter(paymentDate__gte = startDate(), paymentDate__lte = finishDate()).aggregate(Count('amount'))

    })

"""       
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
        })"""

def addpayment(request):
    return render(request, "search/addpayment.html", {
        'paymentKinds': PaymentsKind.objects.order_by('id'),
        'supplyers': Supplyer.objects.order_by('supplyerName'),
        'statuses': Status.objects.order_by('id')
    }
    )




def payment(request, payment_id):
    payment = Payments.objects.get(pk=payment_id)
    return render(request, "search/payment.html", {
        "payment": payment
    })

def addpaymentkind(request):
    if request.method == "POST":
        try:
            form = AddPaymentKindForm(request.POST)
  
            if form.is_valid():
            
                paymentDefinition = form.cleaned_data["definition"]
                newPaymentKind = PaymentsKind(definition=paymentDefinition)
                
                newPaymentKind.save()
                messages.success(request, paymentDefinition + " was successfully added.")
                return HttpResponseRedirect(reverse('search:addpaymentkind'))
            else:
                form=AddPaymentKindForm()
        except IntegrityError:
            messages.error(request, 'This paymentKind already exists: ' + paymentDefinition)
 
       
    
    return render (request, "search/addpaymentkind.html", {
        "form": AddPaymentKindForm(),
        "paymentKinds": PaymentsKind.objects.order_by('id')
    
    })

def addsupplyer(request):
    last_supplyer = Supplyer.objects.last().supplyerCode
    next_supplyer = last_supplyer+1
    if request.method == 'POST':
        new_code = request.POST['new_code']
        newname = request.POST['new_supplyer']
        new_supplyer = Supplyer(supplyerCode=new_code, supplyerName=newname)
        new_supplyer.save()
        next_supplyer +=1
        return render(request, 'search/addsupplyer.html', {
            'supplyers': Supplyer.objects.all(),
            'next_supplyer': next_supplyer
        })
   
    return  render(request, 'search/addsupplyer.html', {
        'supplyers': Supplyer.objects.all(),
        'next_supplyer': next_supplyer
    })