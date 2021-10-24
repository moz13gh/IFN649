from django.db import models
from rest_framework import serializers

# Create your models here.
class Temperature(models.Model):
    temperature_value = models.FloatField()
    time_stamp = models.TimeField(auto_now=False, auto_now_add=False)
    severity = models.CharField(max_length=30)


class Air_Quality(models.Model):
    pm25_value = models.FloatField()
    time_stamp = models.TimeField(auto_now=False, auto_now_add=False)
    severity = models.CharField(max_length=30)

class Humidity(models.Model):
    humidity_value = models.FloatField()
    time_stamp = models.TimeField(auto_now=False, auto_now_add=False)
    severity = models.CharField(max_length=30)

class Air_Qualty_Serializer(serializers.Serializer):
    pm25_value = serializers.FloatField()
    time_stamp = serializers.TimeField()
    severity = serializers.CharField()




