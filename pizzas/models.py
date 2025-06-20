from django.db import models

class PizzaModel(models.Model):
    class Meta:
        db_table = 'pizza'
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.FloatField()

