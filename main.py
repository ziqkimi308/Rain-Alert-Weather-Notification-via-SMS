"""
********************************************************************************
* Project Name:  Rain Alert Weather Notification via SMS
* Description:   Rain Alert is a Python-based application that uses the Open Meteo API to fetch weather data and notifies you via SMS if there’s a chance of rain. 
* Author:        ziqkimi308
* Created:       2024-12-16
* Updated:       2024-12-16
* Version:       1.0
********************************************************************************
"""

import requests
from twilio.rest import Client

# CONSTANT
# --------------------- CHANGE WEATHER API HERE -------------------------------- #
API_ENDPOINT = "https://api.open-meteo.com/v1/forecast" # Use Open Meteo
API_KEY = ""
# --------------------- CHANGE TWILIO DETAILS HERE ----------------------------- #
ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
TARGET_PHONE_NUMBER = ""


parameters = {
	"latitude": -10.665510, # Location: Songea, Tanzania
	"longitude": 35.645039,
	"hourly": "weather_code",
	"timezone": "auto"
}

# Modify and customize data to what we need
response = requests.get(url=API_ENDPOINT, params=parameters)
print(response.status_code)
weather_data = response.json()
weather_code_sliced = weather_data["hourly"]["weather_code"][7:19]

# Trigger Rain Status
will_rain = False
for code in weather_code_sliced:
	if int(code) > 48:
		will_rain = True

# SMS Setup
if will_rain:
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(
    body="Today might be raining. Bring ☔",
    from_=TWILIO_PHONE_NUMBER,
    to=TARGET_PHONE_NUMBER
	)
	print(message.status)
