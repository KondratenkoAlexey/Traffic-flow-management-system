from django.db import models


class Operator(models.Model):
    name = models.CharField(blank=False, max_length=15)
    login = models.CharField(blank=False, max_length=15)
    password = models.CharField(blank=False, max_length=15)

    def __str__(self):
        return self.name


class Truck(models.Model):
    PROCEDURE_TYPE = {"l": "Погрузка", "u": "Разгрузка"}
    WAREHOUSE_NUMBER = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E")]
    RAMP_NUMBER = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9)]
    STATE = {"r": "Зарегистрирован", "e": "Въезд", "d": "Выезд"}
    OPERATOR_COMMAND = [("call", "Вызвать"), ("entered", "Въехал"), ("arrived", "Прибыл"), ("serviced", "Обслужен"), ("departure", "Выехал")]

    truck_number = models.CharField(blank=False, max_length=15, primary_key=True, unique=True)
    phone_number = models.CharField(blank=False, max_length=20)
    company = models.CharField(blank=False, max_length=200)
    procedure = models.CharField(blank=False, max_length=10)
    warehouse = models.CharField(max_length=1, choices=WAREHOUSE_NUMBER)
    ramp = models.CharField(max_length=1, choices=RAMP_NUMBER)
    registration_time = models.DateTimeField()
    entry_time = models.DateTimeField(null=True)
    departure_time = models.DateTimeField(null=True)
    state = models.CharField(max_length=1)
    command = models.CharField(null=True, max_length=10, choices=OPERATOR_COMMAND)

    def __str__(self):
        return self.truck_number
