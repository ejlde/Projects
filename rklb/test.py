import json,statistics

# 1) "Retrieving" json data from Leolabs api
#import requests
#url = 'https://api.leolabs.space/v1/catalog/conjunctions/screenings/54278'

#response = requests.get(url)
#response.raise_for_status()
#data = json.loads(response.text)


# 2) Processing the response JSON
with open('screening_metadata.json',encoding = "utf-8") as f:
    data = json.load(f)  # dictionary
    #keys = []
    #vals = []
    #print(data.keys()) #
    # print(data['screeningParameters']) 


    

    #print(sources)
    #pg = temp['perigee']
    #print(data['catalog'][0]) # this has all the data
    #print(type(temp))
    #minPerigee = min()
    
    #print(data.values())
    # "catalogSize": 26949
    # "primaryCatalogNumber": "L130687",
    

# 3) Print the status of the screening & whether there are any CDMs.
# The output should include
# 
# a) expected collisions,
# 
# print("The expected number of collisions is: ", data['expectedCollisions'])
# 
# b) number of objects screened
#
# print("The number of objects screened is : " , data['catalogSize'])
#
# c) min/max/median perigee of objects,
#
# catalogs = data['catalog']
#    perigees = []
#    sources = []
#    for temp in catalogs:
#        perigees.append(temp['perigee'])
#        sources.append(temp['source'])
    # print(min(perigees))
    # print(max(perigees))
    # print(statistics.median(perigees))
# 
# 
#  d) list of data sources used
#     print(sources)


# Closing file
#f.close()
