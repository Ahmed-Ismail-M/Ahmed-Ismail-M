"""
module doc
"""
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """ override user"""
    "to do"
class Customer:
    """ CUSTOMER MODEL"""
    id : int
    name: str
    def __str__(self) -> str:
        return f"id is the number of {self.id} and the name is {self.name}"
