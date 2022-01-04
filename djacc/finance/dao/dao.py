""" dao"""
from finance.interface import IEntityDAO
from finance.models import Customer

class CustomerDAO(IEntityDAO):
    """ CUSTOMER DAO"""
    @staticmethod
    def get_all(name: str):
        """ RETRIEVE ALL """
        new_customer = Customer()
        new_customer.id = 20
        new_customer.name = name
        return new_customer.__dict__
    