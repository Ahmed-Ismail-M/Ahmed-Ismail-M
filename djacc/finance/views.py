"""
module doc
"""
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from finance.models import Customer
from finance.forms.forms import NewTransferForm
# Create your views here.
def customers(request):
    """ rout customers"""
    return render(request, "customers.html", {"customers":Customer.objects.all()})

def home(request):
    """ rout home"""
    return render(request, "home.html")

def transfer(request, cust_id):
    customer = Customer.objects.get(pk=cust_id)
    if request.method == "POST":
        form = NewTransferForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            print(amount)
            return HttpResponseRedirect(reverse("finance:cust"))
        else:
            return render(request, "transfer.html", {
        "form":form
    })

    return render(request, "transfer.html", {
        "form":NewTransferForm(), "customer":customer
    })