from django.db import models
from django.db.models.fields.related import ForeignKey
from rest_framework import serializers

# Create your models here.
class Temperature_Reading(models.Model):
    temperature_value = models.FloatField()
    time_stamp = models.TimeField(auto_now=False, auto_now_add=False)
    date_stamp = models.DateField(auto_created=True)
    severity = models.CharField(max_length=30)

class Air_Quality_Reading(models.Model):
    pm25_value = models.FloatField()
    time_stamp = models.DateTimeField()
    severity = models.CharField(max_length=30)

class Humidity_Reading(models.Model):
    humidity_value = models.FloatField()
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_stamp = models.DateField(auto_created=True)
    severity = models.CharField(max_length=30)

class Peripheral(models.Model):
    categories = (
        ("Air Purifier", "Air Purifier"),
        ("Dehumidifier", "Dehumidifier"),
        ("Air Conditioner", "Air Conditioner"),
        ("Fan", "Fan"),
        ("Window", "Window")
    )

    activities = (
        ("Standby", "Standby"),
        ("Active", "Active"),
        ("Sleep", "Sleep"),
    )

    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=categories)
    online_status = models.BooleanField()
    activity_status = models.CharField(max_length=30, choices=activities)

class Action(models.Model):
    peripheral_id = models.IntegerField()
    action = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_created=False, auto_now=False, auto_now_add=False)
    date_stamp = models.DateField(auto_created=True)


# class Air_Qualty_Serializer(serializers.Serializer):
#     pm25_value = serializers.FloatField()
#     time_stamp = serializers.TimeField()
#     severity = serializers.CharField()




