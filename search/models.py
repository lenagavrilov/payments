from django.db import models

# Create your models here.


class Supplyer(models.Model):
    supplyerName = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.supplyerName}"

class Status(models.Model):
    definition = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.definition}" 

class PaymentsKind(models.Model):
    definition = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.definition}"


class Payments(models.Model):
    paymentKind = models.ForeignKey(PaymentsKind, on_delete=models.PROTECT, related_name="paymentKind")
    checkNumber = models.IntegerField(blank=True)
    amount = models.IntegerField(default=0)
    paymentDate = models.DateField()
    supplyer = models.ForeignKey(Supplyer, on_delete=models.PROTECT, related_name="supplyer")
    details = models.CharField(max_length=200, blank=True)
    givenOutDate = models.DateField(blank=True)
    paymentNumberInSeries = models.IntegerField(blank=True)
    quantityinSeries = models.IntegerField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status')
    refuseReason = models.CharField(max_length=64, blank=True)
    refuseDate = models.DateField(max_length=64, default='1900-01-01')
    givenInstead = models.CharField(max_length=200, blank=True)
    alternativeSupplyer = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"Payment Kind {self.paymentKind}, Check number {self.checkNumber} -  to be paid on {self.paymentDate}."



