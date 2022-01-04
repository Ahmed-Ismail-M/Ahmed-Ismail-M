"""
module doc
"""
from django.shortcuts import render
from .dao.dao import CustomerDAO
# Create your views here.
def customers(request, name:str):
    """ rout customers"""
    return render(request, "customers.html", CustomerDAO.get_all(name=name))

def home(request):
    """ rout home"""
    return render(request, "home.html")