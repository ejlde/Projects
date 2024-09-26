"""
Created by: Eric Dean
Created on: 11/18/2023
Comment: The purpose of this script is to "retrive" json data
from the LeoLabs api, process the expected response json from that api,
then evaluate and print the status of that response.
"""
import json
import statistics

# 1) "Retrieving" json data from Leolabs api
#import requests
#url = 'https://api.leolabs.space/v1/catalog/conjunctions/screenings/54278'

#response = requests.get(url)
#response.raise_for_status()
#data = json.loads(response.text)

# 2) Processing the response JSON
with open('screening_metadata.json',encoding = "utf-8") as f:
    data = json.load(f)
    catalogs = data['catalog']
    perigees = []
    sources = []
    for temp in catalogs:
        perigees.append(temp['perigee'])
        if temp['source'] not in sources:
            sources.append(temp['source'])

# 3) Print the status of the screening & whether there are any CDMs.
# a) expected collisions,
print("The expected number of collisions is: ", data['expectedCollisions'])
# b) number of objects screened
print("The number of objects screened is: " , data['catalogSize'])
# c) min/max/median perigee of objects,
print("The minimum perigee is: " , min(perigees))
print("The maximum perigee is: " , max(perigees))
print("The median perigee is: " , statistics.median(perigees))
#  d) list of data sources used
print("The list of data sources used is: ", sources)
