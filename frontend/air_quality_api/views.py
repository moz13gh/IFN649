from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
# Create your views here.

def getAPIData(request):
    pm25_data = getPM25()
    humidity_data = getHumidity()
    temperature_data = getTemperature()

    context = {
        "pm25_data": pm25_data,
        "humidity_data": humidity_data,
        "temperature_data": temperature_data
    }

    return render(request, "air_quality_api/index.html", context)


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
    print(" humidity (in percentage) = " + str(current_humidity))

    return response.json()

def getTemperature():
    response = requests.get('https://www.tianqiapi.com/free/day?appid=62141163&appsecret=DLW3gPlK&unescape=1')
    response.encoding="utf-8"#print(response.text)print (response.json())

    print('return results: %s'% response.json())

    print('City:%s'%response.json()['city'])

    print ('Temperature: %s' %response.json() ['tem'] + '°C')

    return response.json()