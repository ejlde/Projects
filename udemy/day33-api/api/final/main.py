import requests
from datetime import datetime, timezone, timedelta
import time
import smtplib

MY_LAT = 33.797119 # Your latitude
MY_LONG = -118.168358 # Your longitude
MY_EMAIL = ""
MY_PASSWORD = ""

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    coords_diff(MY_LAT,MY_LONG,iss_latitude,iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.
def coords_diff(my_lat,my_long,iss_lat,iss_long):
    lat_diff = abs(iss_lat - my_lat)
    long_diff = abs(iss_long - my_long)
    print(f"the lat diff = {lat_diff}")
    print(f"the long diff = {long_diff}")
    return True if (lat_diff < 5.0 and long_diff < 5.0) else False

def is_dark(time_now,sunrise_hour,sunset_hour):
    return True if(time_now.hour > sunset_hour or time_now.hour < sunrise_hour) else False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 7
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 7
    time_now = datetime.now(timezone.utc) - timedelta(hours=7)
    is_dark(time_now,sunrise,sunset)


#If the ISS is close to my current position +- 5 deg of ISS
    
# and it is currently dark


# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg = "Subject: Look Up👆\n\nThe ISS is above you in the sky."
        )
    
# BONUS: run the code every 60 seconds.



