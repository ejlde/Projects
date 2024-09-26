import requests
from datetime import datetime,timezone

MY_LAT = 33.797119
MY_LONG = -118.168358
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)

time_now  = datetime.now()

print(time_now)