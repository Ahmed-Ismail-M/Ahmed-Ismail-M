"""
module doc
"""
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from finance.models import Customer
from finance.forms.forms import NewTransferForm


# Create your views here.
def customers(request):
    """ rout customers"""
    return render(request, "customers.html", {"customers": Customer.objects.all()})


def home(request):
    """ rout home"""
    return render(request, "home.html")


def transfer(request, cust_id):
    customer_from = Customer.objects.get(pk=cust_id)
    choices = list(Customer.objects.exclude(id=cust_id).values_list("id", "first_name"))
    if request.method == "POST":
        form = NewTransferForm(choices=choices, max_value=float(customer_from.balance), data=request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            customer_to = Customer.objects.get(pk=form.cleaned_data["cust_name"])
            customer_to.balance = customer_to.balance+ amount
            customer_from.balance = customer_from.balance - amount
            customer_to.save()
            customer_from.save()
            return HttpResponseRedirect(reverse("finance:cust"))
        else:
            return render(request, "transfer.html", {
                "form": form, "customer": customer_from
            })

    return render(request, "transfer.html", {
        "form": NewTransferForm(choices=choices, max_value=float(customer_from.balance)), "customer": customer_from
    })
