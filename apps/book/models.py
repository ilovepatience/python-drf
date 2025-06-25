from django.db import models
from core.models import BaseModel

class BookModel(BaseModel):
    class Meta:
        db_table = 'book'
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    rating = models.FloatField()