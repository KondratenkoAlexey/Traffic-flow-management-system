from django import forms
from .models import Truck


class Loading(forms.Form):
    truck_number = forms.CharField(max_length=15, label="Госномер автомобиля")
    phone_number = forms.CharField(max_length=15, label="Номер телефона")
    company = forms.CharField(max_length=200, label="Компания")


class Unloading(forms.Form):
    truck_number = forms.CharField(max_length=15, label="Госномер автомобиля")
    phone_number = forms.CharField(max_length=15, label="Номер телефона")
    company = forms.CharField(max_length=200, label="Компания")


class Operator_control(forms.Form):
    truck_number = forms.CharField(max_length=15, label="Госномер автомобиля")
    warehouse = forms.ChoiceField(choices=Truck.WAREHOUSE_NUMBER, label="Склад")
    ramp = forms.ChoiceField(choices=Truck.RAMP_NUMBER, label="Рампа")
    command = forms.ChoiceField(choices=Truck.OPERATOR_COMMAND, label="Действие")
