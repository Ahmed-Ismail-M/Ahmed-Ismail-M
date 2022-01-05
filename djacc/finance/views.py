"""
module doc
"""
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from finance.forms.forms import NewTransferForm
from .dao.dao import CustomerDAO
# Create your views here.
def customers(request):
    """ rout customers"""
    return render(request, "customers.html", CustomerDAO.get_all(name="ahned"))

def home(request):
    """ rout home"""
    return render(request, "home.html")

def transfer(request):
    if request.method == "POST":
        form = NewTransferForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            print(amount)
            return HttpResponseRedirect(reverse("finance:transfer"))
        else:
            return render(request, "transfer.html", {
        "form":form
    })
    return render(request, "transfer.html", {
        "form":NewTransferForm()
    })