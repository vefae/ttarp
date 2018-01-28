from __future__ import unicode_literals
from django.db import models


# Create your models here.


class inventory (models.Model):
    
    inv_name = models.CharField(max_length=140)
    notes = models.TextField()

    def __str__(self):
        return self.inv_name
