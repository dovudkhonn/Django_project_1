from django.contrib import admin
from apps.cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "color", "number", "type"]


admin.site.register(Car, CarAdmin)
