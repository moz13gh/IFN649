from django.shortcuts import render
import requests
from preprocessing.models import *
from preprocessing.views import *


# Create your views here.
def getProcessedData(request):

    # Call API call in preprocessing here. 
    getAPIData()    

    # Prepare Context for UI Page.
    peripherals_list = list(Peripheral.objects.values())
    
    # actions_list = []

        # GET the most recent action of each device type
    # for item in peripherals_list:
    #     temp = Action.objects.filter(peripheral_id=item["id"]).latest("time_stamp").values()
    #     actions_list.append(temp)

    # print(actions_list[0].action)

    current_humidity = Humidity_Reading.objects.latest('time_stamp')
    current_air_quality = Air_Quality_Reading.objects.latest('time_stamp')
    current_temperature = Temperature_Reading.objects.latest('time_stamp')



    context = {
        "peripherals_list": peripherals_list,
        "current_humidity": current_humidity,
        "current_air_quality": current_air_quality,
        "current_temperature": current_temperature,
        # "actions_list": actions_list
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

