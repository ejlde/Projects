
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
jday_data = []
scid = [1,2,3,4,5,6,\
        6,2,3,1,5,4,\
        1,2,3,4,5,6] # 18 contacts
gnd = ['DEN','LA','SYD','LON','LA','DEN',\
       'SYD','LON','LON','DEN','LA','SYD',\
        'SYD','LON','DEN','LA','LA','DEN']
ele = [57.9,8.3,11.1,45.4,22.1,28.5,\
       41.2,55.4,67.2,12.7,33.3,54.2,\
        10.9,11.3,31.7,33.8,57.7,41.6]
for i in range(3,21): # 3 to 21 minutes ahead 
    d = timedelta(minutes = i )
    d1 = timedelta(minutes = i + random.randint(4,9))
    # Edge case where the time can be close to 0 (AOS) but jday is the same
    # update jday based on aos -- done
    jday_data.append((now+d).timetuple().tm_yday) # jday
    aos_data.append(now + d) # aos/los are currently full dts whereas in the emails its just a time
    los_data.append(now + d1)


data = []
for i in range(0,len(aos_data)):
    contact = [jday_data[i],aos_data[i],los_data[i],scid[i],gnd[i],ele[i]]
    # used to have jday = problematic when trying to use regular(actual) methodology
    data.append(contact)
#print(jday_data)

def contact_schedule(num_contacts,scid_list):

    new_now = dt.now(timezone.utc).replace(microsecond=0)
    new_now = dt(new_now.year,new_now.month,new_now.day,\
                 new_now.hour,new_now.minute,new_now.second) # aware -> naive

    # Finding upcoming & active contacts
    td = []
    flag = []
    dur = []
    data_final = []
    for x in range(len(data)):

        contact_scid = data[x][3]

        if contact_scid in scid_list:
            contact_jday = str(data[x][0]) # only jday is given in emails
            contact_aos = str(data[x][1].time())
            contact_los = str(data[x][2].time()) # only time is given in emails


            aos_full_str = contact_jday + ' ' + contact_aos # string format
            los_full_str = contact_jday + ' ' + contact_los

            los_full_00 = dt.strptime(los_full_str,'%j %H:%M:%S') # 1900
            aos_full_00 = dt.strptime(aos_full_str,'%j %H:%M:%S')
            los_full_pres = dt(now.year,los_full_00.month,los_full_00.day,\
                               los_full_00.hour,los_full_00.minute,los_full_00.second)
            aos_full_pres = dt(now.year,aos_full_00.month,aos_full_00.day,\
                               aos_full_00.hour,aos_full_00.minute,aos_full_00.second)

            td_temp = (los_full_pres - aos_full_pres).total_seconds() # negative = day change
            # dur_temp = los_full_pres - aos_full_pres

            # Jday Change Condition
            if td_temp < 0:
                jd_change = now + timedelta(days=1)
                los_full_pres = dt(jd_change.year,jd_change.month,jd_change.day,\
                                   los_full_00.hour,los_full_00.minute,los_full_00.second)
        

            aos_td = (aos_full_pres - new_now)
            los_td = (los_full_pres - new_now)

            if aos_td.total_seconds() > 0: # Upcoming
                data_final.append(data[x])
                td.append(aos_td)
                flag.append("\u274C") # x emoji
                dur.append(td_temp)
            elif los_td.total_seconds() >= 0: # Active
                data_final.append(data[x])
                td.append(los_td)
                flag.append("\u2705") # green check emoji
                dur.append(td_temp)
    if num_contacts == 0:
        num_contacts = len(data_final) # ?? double check
    aos = []
    los = []
    scid = []
    gnd = []
    ele = []
    durf = []
    act = []
    tl = []
    for x in range(num_contacts):
        aos.append(data_final[x][1].time())
        los.append(data_final[x][2].time())
        scid.append(data_final[x][3])
        gnd.append(data_final[x][4])
        ele.append("{0:.1f}".format(data_final[x][5]))
        durf.append(dur[x])
        act.append(flag[x])
        tl.append(str(td[x]))
    """
    print("The len of aos is: ", len(aos))
    print("The len of los is: ", len(los))
    print("The len of scid is: ", len(scid))
    print("The len of gnd is: ", len(gnd))
    print("The len of ele is: ", len(ele))
    print("The len of dur is: ", len(dur))
    print("The len of act is: ", len(act))
    print("The len of tl is: ", len(tl))
    """
    
    keys = ["SCID","AOS","LOS","Ground Site","Max Elevation","Duration","Active","Time Left"]
    vals = [scid,aos,los,gnd,ele,dur,act,tl]
    res = dict(zip(keys,vals))
    df = pd.DataFrame(res)
    return df[["SCID","AOS","LOS","Ground Site","Max Elevation","Duration","Active","Time Left"]]

"""
num_contacts = 9
scid_list = [1,2,3,4,5,6]
out = contact_schedule(num_contacts,scid_list)
"""

