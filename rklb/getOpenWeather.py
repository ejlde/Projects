# username = ejldean13
# email = ejldean13@gmail.com   
# pw = Ejldean0207*

import json, requests, sys

# API key = 868ec1db57652dc0f0f56529633550ca

APPID = '868ec1db57652dc0f0f56529633550ca'
'''
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:]) # join city & country name
'''
location = 'Denver,US'
# Download JSON data from OpenWeatherMap.org's API
# q=London,uk&APPID=868ec1db57652dc0f0f56529633550ca
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' %(location,APPID)
# url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' %(location,APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw json text:
#print(response.text)

# Load json data into a python variable
weatherData = json.loads(response.text)
print(weatherData.keys())
print(weatherData.values())
#print(weatherData)
