from django.contrib import admin
from src.invoice.models import CustomerModel, BillModel, PurchasedProductModel

admin.site.register(CustomerModel)
admin.site.register(BillModel)
admin.site.register(PurchasedProductModel)

