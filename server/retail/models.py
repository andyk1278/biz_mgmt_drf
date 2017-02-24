from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Chain(models.Model):
    """ retail chain model"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    slogan = models.CharField(max_length=1000)
    founded_date = models.CharField(max_length=500)
    website = models.URLField(max_length=500)


class Store(models.Model):
    """ Store location model. Foreign key to its Chain"""
    chain = models.ForeignKey(Chain)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    opening_date = models.DateTimeField(default=timezone.now)
    #Business hours in a 24 hour clock. Deafult 8am-5pm
    business_hours_start = models.IntegerField(
        default=8,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(23)
        ]
    )

class Employee(models.Model):
    """ Employee model. Foreign key to its Store"""
    store = models.ForeignKey(Store)
    number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hired_date = models.DateTimeField(default=timezone.now)