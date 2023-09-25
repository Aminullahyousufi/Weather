import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "69f04e4613056b159c2761a9d9e664d2"

account_sid = "AC74e0ee69d3c127fc518ce41b33325432"
auth_token = "6f6824b981f5c3fb1338bb2a5b1b4d0f"

weather_params = {
    "lat": 60.152988,
    "lon": -1.149293,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hello, It is going to get hot. Please turn on the cooler",
        from_='+12512415488',
        to='+33753910921'
    )

    print(message.status)
