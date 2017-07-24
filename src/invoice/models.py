from django.db import models
from django.utils import timezone

from src.inventory.models import ProductModel

MODE_OF_PAYMENT_CHOICES = (
    ('CSH', 'CASH'),
    ('Cr', 'CREDIT CARD'),
    ('Dr', 'DEBIT CARD'),
    ('OTH', 'OTHER')
)


class CustomerModel(models.Model):
    mob_no = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    customer_credit = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.customer_name)


class TempPurchasedProductModel(models.Model):
    temp_prod_id = models.AutoField(primary_key=True, )
    product_id = models.ForeignKey(ProductModel)
    qty = models.IntegerField()


class PurchasedProductModel(models.Model):
    purchased_id = models.AutoField(primary_key=True)
    temp_product_id = models.ForeignKey(TempPurchasedProductModel)
    Total_Amount = models.DecimalField()


class BillModel(models.Model):
    bill_no = models.AutoField(primary_key=True)
    purchased_id = models.ForeignKey(PurchasedProductModel)
    Shop_details = models.TextField(default="ABC LTD. TN No: XXX Address: Jaipur Mob:XXXXXXXXXXX")
    mode_of_payment = models.CharField(max_length=3, choices=MODE_OF_PAYMENT_CHOICES, default='CSH',
                                       verbose_name='Payment Mode')
    other_payment_option = models.CharField(max_length=30, blank=True, default=None)
    mob = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, default=0)
    datetime = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.bill_no)
