
import requests
from twilio.rest import Client
import os

url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get(OWM_API_KEY)"25c0d220fab65828e357daf5b98d4aec"

account_sid = "ACa18ae9347242d9fcacb58d30d149187b"
auth_token = "e7226902132fe8acc7d2aab69729a876"

params = {
    "lat": 22.565571,
    "lon": 88.370209,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=url, params=params)
# print(response.raise_for_status())

data = response.json()
weather_slice = data["hourly"][0:12]

will_rain = False

for hourly_weather in weather_slice:
    weather_id = hourly_weather["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, bring an umbrella",
        from_="+14252767491",
        to="+919836125552",
    )

    print(message.status)
