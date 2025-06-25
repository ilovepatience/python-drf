from django.db import models

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'car'
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.FloatField()


