from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name
