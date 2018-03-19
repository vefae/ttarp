from __future__ import unicode_literals
from django.db import models




class equipment (models.Model):

    equipment_name = models.CharField(max_length=140)
    category = models.CharField(max_length=140)
    plate = models.CharField(max_length=140)
    brand = models.CharField(max_length=140)
    engine_no = models.IntegerField()
    hourly_fuel_consumption = models.IntegerField()
    fuel_type = models.CharField(max_length=140)
    purchase_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.equipment_name
