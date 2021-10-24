from django.shortcuts import render
import requests
from .models import *
from .actions import *
# Create your views here.

def getAPIData():

    pm25_data = getPM25()
    humidity_data = getHumidity()
    temperature_data = getTemperature()

    pm25_value = pm25_data["data"]["iaqi"]["pm25"]["v"]
    severity = getPM25Severity(pm25_value)

    pm25_entry = Air_Quality_Reading(pm25_value=pm25_value, severity=severity)
    pm25_entry.save()

    humidity_value = humidity_data["main"]["humidity"]
    severity = getHumiditySeverity(humidity_value)

    humidity_entry = Humidity_Reading(humidity_value=humidity_value, severity=severity)
    humidity_entry.save()
    
    temperature_value = temperature_data["tem"]
    severity = getTemperatureSeverity(temperature_value)
    
    temperature_entry = Temperature_Reading(temperature_value=temperature_value, severity=severity)
    temperature_entry.save()

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

def getHumidity():
    api_key = "68dcff5910beef2a5bb794c2c9417ee7"
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Give city name
    city_name = "hongkong"
    # Get data using the get() function. It needs a completed API Request URL
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    # response.josn() provides the result of your API call.
    x = response.json()
    # store the value of "main"
    # key in variable y
    y = x["main"]
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
    # print following values
    # print(" humidity (in percentage) = " + str(current_humidity))
    return response.json()

def getTemperature():
    response = requests.get('https://www.tianqiapi.com/free/day?appid=62141163&appsecret=DLW3gPlK&unescape=0$cityid=101320101')
    response.encoding="utf-8"#print(response.text)print (response.json())

    # print('return results: %s'% response.json())

    # print('City:%s'%response.json()['city'])

    # print ('Temperature: %s' %response.json() ['tem'] + '°C')

    return response.json()

def getPM25Severity(value):
    value = int(value)

    if value >= 0 and value < 50:
        # controlWindows("on")
        # controlAirPurifier("off")
        return "Good"
    
    if value > 50 and value < 100:
        # controlWindows("on")
        # controlAirPurifier("off")
        return "Moderate"

    if value > 100 and value < 150:
        # controlWindows("off")
        # controlAirPurifier("off")
        return "Unhealthy for Sensitive Groups"

    if value > 150 and value < 200:
        # controlWindows("off")
        # controlAirPurifier("on")
        return "Unhealthy"

    if value > 200 and value < 300:
        # controlWindows("off")
        # controlAirPurifier("on")
        return "Very Unhealthy"

    if value > 300:
        # controlWindows("off")
        # controlAirPurifier("on")
        return "Hazardous"

def getHumiditySeverity(value):

    value = float(value)

    if value < 40:
        # controlWindows("on")
        # controlDehumidifier("off")
        return "Low Humidity"

    if value >40 and value < 60:
        # controlWindows("on")
        # controlDehumidifier("off")
        return "Normal"

    if value > 60:
        # controlWindows("off")
        # controlDehumidifier("on")
        return "High Humidity"

def getTemperatureSeverity(value):

    value = float(value)

    if value < 15:
        return "Low Temperature"

    if value > 15 and value < 26:
        return "Optimal Temperature"

    if value > 26 and value < 30:
        return "Moderately High Temperature"

    if value > 30:
        return "Very High Temperature"