from django.db import models
from apps.utils.model_statuses import CarColors, CarTypes


class Car(models.Model):
    model = models.CharField(max_length=100)
    color = models.IntegerField(choices=CarColors.choices)
    number = models.CharField(max_length=15)
    type = models.IntegerField(choices=CarTypes.choices)
