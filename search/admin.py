from django.contrib import admin

from .models import Payments, PaymentsKind, Supplyer, Status

# Register your models here.

class SupplyerAdmin(admin.ModelAdmin):
    list_display = ("id", "supplyerName")


admin.site.register(Payments)
admin.site.register(PaymentsKind)
admin.site.register(Supplyer, SupplyerAdmin)
admin.site.register(Status)