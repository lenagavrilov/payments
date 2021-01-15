from django.db import models

# Create your models here.
class PaymentsKind(models.Model):
    definition = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.id}: {self.definition}"

class Supplyer(models.Model):
    supplyerName = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.id}: {self.supplier}"

class Status(models.Model):
    definition = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}: {self.definition}"


class Payments(models.Model):
    paymentKind = models.ForeignKey(PaymentsKind, on_delete=models.PROTECT, related_name="paymentsKind")
    checkNumber = models.IntegerField()
    amount = models.IntegerField(default=0)
    paymentDate = models.DateField()
    supplier = models.ForeignKey(Supplyer, on_delete=models.PROTECT, related_name="supplyer")
    details = models.CharField(max_length=200)
    givenOutDate = models.DateField()
    paymentNumberInSeries = models.IntegerField()
    quantityinSeries = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status')
    refuseReason = models.CharField(max_length=64)
    refuseDate = models.CharField(max_length=64)
    givenInstead = models.CharField(max_length=200)
    alternativeSupplier = models.CharField(max_length=64)

    def __str__(self):
        if self.paymentKind != 1:
            return f" {self.paymentKind} -  to be paid on {self.paymentDate}."
        else:
            return f"Check number {self.checkNumber} -  to be paid on {self.paymentDate}."



