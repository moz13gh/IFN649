from django.shortcuts import render
import requests
from preprocessing.models import *
from preprocessing.views import *


# Create your views here.
def getProcessedData(request):

    # Call API call in preprocessing here. 
    getAPIData()

    peripherals_list = list(Peripheral.objects.values())
    # TODO: Get current data / most recent data
    current_humidity = list(Humidity_Reading.objects.values())
    current_air_quality = list(Air_Quality_Reading.objects.values())
    current_temperature = list(Temperature_Reading.objects.values())
    actions = list(Action.objects.values())

    context = {
        "peripherals_list": peripherals_list,
        "current_humidity": current_humidity,
        "current_air_quality": current_air_quality,
        "current_temperature": current_temperature,
        "actions": actions
    }

    return render(request, "cloud_ui/index.html", context)


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
    print("Location: " + location)
    print("Time Stamp: " + timeStamp)
    print("PM2.5 Rating: " + str(pm25Rating) + "\n")

    return response.json()


def getSettings(request):
    return render(request, "cloud_ui/settings.html")

