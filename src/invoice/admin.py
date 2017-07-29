from django.contrib import admin
from invoice.models import CustomerModel, BillModel, PurchasedProductModel, TempPurchasedProductModel, ProductPurchasedRelation

admin.site.register(CustomerModel)
admin.site.register(BillModel)
admin.site.register(PurchasedProductModel)
admin.site.register(TempPurchasedProductModel)
admin.site.register(ProductPurchasedRelation)



