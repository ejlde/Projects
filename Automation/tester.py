
# Importing modules
from datetime import timezone,timedelta,datetime as dt
#import win32com.client as win
import warnings
import random
import pandas as pd
import pytz
import streamlit as st
import time

warnings.simplefilter(action='ignore',category=FutureWarning)

# Creating Fake Data
# JDAY, AOS, LOS, SCID GND REV MAXE
global data 
now = dt.now(timezone.utc).replace(microsecond=0)
UTC = pytz.utc

jday = now.timetuple().tm_yday


aos_data = []
los_data = []
scid = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
gnd = ['DEN','LA','SYD','LON','LA','DEN',\
       'SYD','LON','LON','DEN','LA','SYD',\
        'SYD','LON','DEN','LA','LA','DEN']
ele = [57.9,8.3,11.1,45.4,22.1,28.5,\
       41.2,55.4,67.2,12.7,33.3,54.2,\
        10.9,11.3,31.7,33.8,57.7,41.6]
for i in range(3,21): # 3 to 11 minutes ahead
    d = timedelta(minutes = i )
    d1 = timedelta(minutes = i + random.randint(4,9))
    aos_data.append(now + d)
    los_data.append(now + d1)
data = []
for i in range(0,len(aos_data)):
    contact = [jday,aos_data[i],los_data[i],scid[i],gnd[i],ele[i]]
    data.append(contact)

def contact_schedule(num_contacts):

    new_now = dt.now(timezone.utc).replace(microsecond=0)

    # Finding upcoming & active contacts
    data_final = []
    for x in range(len(data)):
        contact_los = data[x][2]
        contact_jday = data[x][0]
        if(contact_jday == jday and contact_los.time() >= new_now.time()):
            data_final.append(data[x])
        elif(contact_jday > jday):
            data_final.append(data[x])
    print(data_final[0])


out = contact_schedule(8)
