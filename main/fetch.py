import os
from requests import get
# Optional - loads API key stored in a separate .env file. For security.
from dotenv import load_dotenv

def getPM25():
    # Variables for constructing the API Call
    path = "https://api.waqi.info/feed/"
    city = "hongkong/"
    apiToken = os.getenv("pm25_api_token")

    # Get data using the get() function. It needs a completed API Request URL
    response = get(path + city + "?token=" + apiToken)

    # response.josn() provides the result of your API call. 
    payload = response.json()["data"]

    # These variables break down the JSON data and gathers the important/useful into. 
    location = payload["city"]["name"]
    timeStamp = payload["time"]["s"]
    pm25Rating = payload["iaqi"]["pm25"]["v"]

    # Print the result of the data to ensure that the API call worked. 
    print("Location: " + location)
    print("Time Stamp: " + timeStamp)
    print("PM2.5 Rating: " + str(pm25Rating) + "\n")

def getHumidity():
    # Look at the .env file
    apiToken = os.getenv("humidity_api_token")
    
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

def getTemperature():
    # Save the api key to the .env file following the format of what is already there.
    apiToken = os.getenv("temperature_api_token")
    

    response = requests.get('https://www.tianqiapi.com/free/day?appid=62141163&appsecret=DLW3gPIK&unescape=1')
    response.encoding="utf-8"#print(response.text)print (response.json())

    print('return results: %s'% rep.json())

    print('City:%s'%rep.json()['city'])

    print (temp: %s' %rep.json() ['tem'] + '°C')

def main():
    # If the .env file can be loaded, make the API calls
    if load_dotenv():
        # TODO: Threading.
        getPM25()
        getHumidity()
        getTemperature()


if __name__ == "__main__":
    main()
