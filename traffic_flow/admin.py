from django.contrib import admin
from .models import Truck, Operator


class TruckAdmin(admin.ModelAdmin):
    list_display = ["id", "truck_number", "company", "state"]
    list_display_links = ["id", "truck_number"]
    search_fields = ["truck_number", "company"]


admin.site.register(Truck, TruckAdmin)
admin.site.register(Operator)
