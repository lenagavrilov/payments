
from django.urls import path
from . import views

app_name = "search"
urlpatterns = [
    path("", views.index, name='index'),
    path("addpayment", views.addpayment, name="addpayment"),
    path("<int:payment_id>", views.payment, name="payment"),
    
]