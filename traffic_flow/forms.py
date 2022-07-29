from django import forms
from .models import Truck


class Process(forms.Form):
    truck_number = forms.CharField(max_length=15, label="Госномер автомобиля",
                                   widget=forms.TextInput(attrs={'placeholder': '1234 AA-1'}))
    phone_number = forms.CharField(max_length=15, label="Номер телефона",
                                   widget=forms.TextInput(attrs={'placeholder': '375291112233'}))
    company = forms.CharField(max_length=200, label="Компания")

    def clean_phone_number(self):
        phone_number_data = self.cleaned_data["phone_number"]
        if not phone_number_data.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")
        return phone_number_data


class OperatorControl(forms.Form):
    truck_number = forms.CharField(max_length=15, label="Госномер автомобиля",
                                   widget=forms.TextInput(attrs={'placeholder': '1234 AA-1'}))
    warehouse = forms.ChoiceField(choices=Truck.WAREHOUSE_NUMBER, label="Склад")
    ramp = forms.ChoiceField(choices=Truck.RAMP_NUMBER, label="Рампа")
    command = forms.ChoiceField(choices=Truck.OPERATOR_COMMAND, label="Действие")
