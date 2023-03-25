from django.db import models

from apps.product.models import Product

ORDER_STATUS = [
    (1, 'Order Placed'),
    (2, 'Order Cancelled'),
    (3, 'Delivered'),
]

CURRENCY = [
    (1, "USD"),
    (2, "INR")
]


class Order(models.Model):
    status = models.IntegerField(choices=ORDER_STATUS, default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.IntegerField(choices=CURRENCY, default=1)

    class Meta:
        db_table = "order"


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = "order_items"

