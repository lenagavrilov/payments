from django.shortcuts import render
from django.http import HttpResponse

columnsNames = ["Payment", "Check Number", "Payment Date", "Supplier", "Details", "Given On", "Payment number ...", "Out of...", "Status", 
                "Refuse Reason", "Refuse Date", "Given Instead", "Alternative Supplier", "Checkbook" ]

columnsValues = [10,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Create your views here.
def index(request):
    return render(request, 'search/index.html', {
        "columnsNames": columnsNames,
        "columnsValues": columnsValues
    })

def addpayment(request):
    return render(request, "search/addpayment.html")