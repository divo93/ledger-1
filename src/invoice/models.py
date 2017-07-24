from django.db import models
from inventory.models import ProductModel


class CustomerModel(models.Model):
    mob_no = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    customer_credit = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.customer_name)
