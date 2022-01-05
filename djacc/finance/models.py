"""
module doc
"""
from django.db import models

class Customer(models.Model):
    """ CUSTOMER MODEL"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
