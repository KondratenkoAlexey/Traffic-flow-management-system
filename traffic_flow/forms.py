from django import forms


class Loading(forms.Form):
    truck_number = forms.CharField(max_length=15, label="Госномер автомобиля")
    phone_number = forms.CharField(max_length=15, label="Номер телефона")
    company = forms.CharField(max_length=200, label="Компания")


class Unloading(forms.Form):
    truck_number = forms.CharField(max_length=15, label="Госномер автомобиля")
    phone_number = forms.CharField(max_length=15, label="Номер телефона")
    company = forms.CharField(max_length=200, label="Компания")
