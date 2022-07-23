from django.db import models


class Truck(models.Model):
    PROCEDURE_TYPE = [("l", "loading"), ("u", "unloading")]
    WAREHOUSE_NUMBER = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)]
    RAMP_NUMBER = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9)]
    STATE = [("r", "registered"), ("e", "entry"), ("d", "departure")]

    truck_number = models.CharField(blank=False, max_length=15, primary_key=True, unique=True)
    phone_number = models.CharField(blank=False, max_length=20)
    company = models.CharField(blank=False, max_length=200)
    procedure = models.CharField(blank=False, max_length=10, choices=PROCEDURE_TYPE)
    warehouse = models.CharField(max_length=1, choices=WAREHOUSE_NUMBER)
    ramp = models.CharField(max_length=1, choices=RAMP_NUMBER)
    registration_time = models.DateTimeField()
    entry_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    state = models.CharField(max_length=1, choices=STATE)


class Operator(models.Model):
    name = models.CharField(blank=False, max_length=15)
    login = models.CharField(blank=False, max_length=15)
    password = models.CharField(blank=False, max_length=15)
