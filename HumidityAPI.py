68dcff5910beef2a5bb794c2c9417ee7


# using openweathermap api


import requests, json

# Enter your API key here
api_key = "68dcff5910beef2a5bb794c2c9417ee7"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = "Brisbane"

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()


	# store the value of "main"
	# key in variable y
	y = x["main"]

	
	# store the value corresponding
	# to the "humidity" key of y
	current_humidity = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))

