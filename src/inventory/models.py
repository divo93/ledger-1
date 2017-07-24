from django.db import models

ITEM_CATEGORIES = (
    ('ONE', 'category 1'),
    ('TWO', 'category 2'),
    ('THREE', 'category 3')
)

GST_CHOICES = (
    (0, '0'),
    (5, '5'),
    (12, '12'),
    (18, '18'),
    (28, '28'),
)


class ProductModel(models.Model):
    item_name = models.CharField(primary_key=True, max_length=50, verbose_name='name')
    item_description = models.CharField(blank=True, max_length=200)
    item_price = models.PositiveIntegerField(db_index=True, verbose_name='price')
    item_quantity = models.PositiveIntegerField(default=0, db_index=True, verbose_name='quantity')
    discount_percent = models.PositiveIntegerField(default=0)
    threshold_quantity = models.PositiveIntegerField(default=5)
    item_category = models.CharField(choices=ITEM_CATEGORIES, max_length=10)
    gst = models.FloatField(choices=GST_CHOICES, verbose_name='GST')

    def __str__(self):
        return str(self.item_name)
