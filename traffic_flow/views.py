from django.shortcuts import render, redirect
from .forms import Process, OperatorControl
from .models import Truck
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "ru")


def home(request):
    return render(request, "home.html")


def client(request):
    return render(request, "client.html")


def loading(request):
    if request.method == 'POST':
        current_time = datetime.now()
        form = Process(request.POST, request.FILES)

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
        form = Process
    return render(request, "loading.html", {"form": form})


def unloading(request):
    if request.method == 'POST':
        current_time = datetime.now()
        form = Process(request.POST, request.FILES)

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
        form = Process

    return render(request, "unloading.html", {"form": form})


def operator(request):
    trucks = Truck.objects.all().filter(state__in=['Зарегистрирован', "Вызван", "Въехал"])

    if request.method == "POST":
        form = OperatorControl(request.POST, request.FILES)

        if form.is_valid():

            number = form.cleaned_data["truck_number"]
            truck = Truck.objects.get(truck_number=number)
            truck.command = form.cleaned_data["command"]

            if truck.command == "call":
                truck.warehouse = form.cleaned_data["warehouse"]
                truck.ramp = form.cleaned_data["ramp"]
                truck.state = Truck.STATE["c"]
            elif truck.command == "entered" and truck.state == Truck.STATE["c"]:
                truck.entry_time = datetime.now().strftime("%d-%m-%Y\n%H:%M")
                truck.state = Truck.STATE["e"]
            elif truck.command == "departure" and truck.state == Truck.STATE["e"]:
                truck.departure_time = datetime.now().strftime("%d-%m-%Y\n%H:%M")
                truck.state = Truck.STATE["d"]

            truck.save()
            return redirect("operator_table")
    else:
        form = OperatorControl

    return render(request, "operator_table.html", {"form": form, "trucks": trucks})


def driver(request):
    trucks = Truck.objects.all().filter(state__in=['Зарегистрирован', "Вызван"])

    return render(request, "driver_table.html", {"trucks": trucks})
