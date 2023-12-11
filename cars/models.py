from django.db import models

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    year_prod = models.IntegerField()
    country_prod = models.CharField(max_length=30)
    volume_engine = models.FloatField(max_length=50)
    price = models.IntegerField()
    color = models.CharField(max_length=25)

