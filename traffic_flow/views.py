from django.shortcuts import render, redirect
from .forms import Loading, Unloading
from .models import Truck, Operator
from datetime import datetime


def home(request):
    return render(request, "home.html")


def client(request):
    return render(request, "client.html")


def loading(request):

    if request.method == 'POST':
        current_time = datetime.now()
        form = Loading(request.POST, request.FILES)

        if form.is_valid():
            truck = Truck()
            truck.truck_number = form.cleaned_data["truck_number"]
            truck.phone_number = form.cleaned_data["phone_number"]
            truck.company = form.cleaned_data["company"]
            truck.procedure = Truck.PROCEDURE_TYPE["l"]
            truck.registration_time = current_time
            truck.state = Truck.STATE["r"]

            truck.save()
            return redirect("home")
    else:
        form = Loading
    return render(request, "loading.html", {"form": form})


def unloading(request):

    if request.method == 'POST':
        current_time = datetime.now()
        form = Unloading(request.POST, request.FILES)
        if form.is_valid():
            truck = Truck()
            truck.truck_number = form.cleaned_data["truck_number"]
            truck.phone_number = form.cleaned_data["phone_number"]
            truck.company = form.cleaned_data["company"]
            truck.procedure = Truck.PROCEDURE_TYPE["u"]
            truck.registration_time = current_time
            truck.state = Truck.STATE["r"]

            truck.save()
            return redirect("home")
    else:
        form = Unloading

    return render(request, "unloading.html", {"form": form})


def operator(request):
    return render(request, "base_table.html")
