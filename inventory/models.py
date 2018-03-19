from __future__ import unicode_literals
from django.db import models


# Create your models here.


class inventory (models.Model):

    inv_name = models.CharField(max_length=140)
    category = models.CharField(max_length=140)
    subcategory = models.CharField(max_length=140)
    producer = models.CharField(max_length=140)
    barcode = models.IntegerField()
    package_quantity = models.IntegerField()
    unit = models.CharField(max_length=140)
    reorder_quantity = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return self.inv_name
