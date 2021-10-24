from django.shortcuts import render
from .models import *
import requests
import os
# Create your views here.

def getAPIData(request):

    pm25_data = getPM25()

    pm25_value = pm25_data["data"]["iaqi"]["pm25"]["v"]
    time_stamp = pm25_data["data"]["time"]["s"]
    severity = getPM25Severity(pm25_value)

    pm25_entry = Air_Quality.objects.create(pm25_value=pm25_value, time_stamp=time_stamp, severity=severity)

    # humidity_data = getHumidity()
    # temperature_data = getTemperature()


def getPM25():
    # Variables for constructing the API Call
    path = "https://api.waqi.info/feed/"
    city = "hongkong/"
    # apiToken = os.getenv("pm25_api_token")
    api_key = "1e74e01ff7ca224118c63cee28d1294261a3ead0"
    # Get data using the get() function. It needs a completed API Request URL
    response = requests.get(path + city + "?token=" + api_key)
    # response.json() provides the result of your API call.
    payload = response.json()["data"]
    # These variables break down the JSON data and gathers the important/useful into.
    location = payload["city"]["name"]
    timeStamp = payload["time"]["s"]
    pm25Rating = payload["iaqi"]["pm25"]["v"]
    # Print the result of the data to ensure that the API call worked.
    # print("Location: " + location)
    # print("Time Stamp: " + timeStamp)
    # print("PM2.5 Rating: " + str(pm25Rating) + "\n")
    return response.json()

def getPM25Severity(value):
    if value >= 0 and value < 50:
        return "Good"
    if value > 50 and value < 100:
        return "Moderate"
    if value > 100 and value < 150:
        return "Unhealthy for Sensitive Groups"
    if value > 150 and value < 200:
        return "Unhealthy"
    if value > 200 and value < 300:
        return "Very Unhealthy"
    if value > 300:
        return "Hazardous"
