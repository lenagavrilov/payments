from django.db import models
from datetime import datetime

# Create your models here.


class Supplyer(models.Model):
    supplyerCode = models.IntegerField()
    supplyerName = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.supplyerName}"

class Status(models.Model):
    statusCode=models.IntegerField()
    definition = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.definition}" 

class PaymentsKind(models.Model):
    definition = models.CharField(max_length = 50, unique=True)


    def __str__(self):
        return f"{self.id}"


class Payments(models.Model):
    paymentKind = models.ForeignKey(PaymentsKind, on_delete=models.PROTECT, related_name="paymentKind")
    checkNumber = models.IntegerField(null=True)
    amount = models.FloatField(default=0.00)
    paymentDate = models.DateField()
    supplyer = models.ForeignKey(Supplyer, on_delete=models.PROTECT, related_name="supplyer")
    details = models.CharField(max_length=200, null=True)
    givenOutDate = models.DateField(null=True)
    paymentNumberInSeries = models.IntegerField(null=True)
    quantityinSeries = models.IntegerField(null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status')
    refuseReason = models.CharField(max_length=64, null=True)
    refuseDate = models.DateField(max_length=64,null=True)
    givenInstead = models.CharField(max_length=200,null=True)
    alternativeSupplyer = models.CharField(max_length=64, null=True)
    checkBook = models.IntegerField(null=True)
    updateDate = models.DateField(auto_now=True)

    def __str__(self):
        return f"Payment Kind {self.paymentKind}, Check number {self.checkNumber} -  to be paid on {self.paymentDate}."



