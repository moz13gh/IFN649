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
    pass

def getTemperature():
    pass

def main():
    # If the .env file can be loaded, make the API calls
    if load_dotenv():
        # TODO: Threading.
        getPM25()
        getHumidity()
        getTemperature()


if __name__ == "__main__":
    main()
