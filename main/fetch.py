import os
from requests import get
from dotenv import load_dotenv

if load_dotenv():

    path = "https://api.waqi.info/feed/"
    city = "hongkong/"
    apiToken = os.getenv("pm25_api_token")

    # Get data
    response = get(path + city + "?token=" + apiToken)

    payload = response.json()["data"]

    location = payload["city"]["name"]
    timeStamp = payload["time"]["s"]
    pm25Rating = payload["iaqi"]["pm25"]["v"]

    print("Location: " + location)

    print("Time Stamp: " + timeStamp)

    print("PM2.5 Rating: " + str(pm25Rating) + "\n")