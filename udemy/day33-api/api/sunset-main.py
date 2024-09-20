import requests


MY_LAT = 33.797119
MY_LONG = -118.168358
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(data)
