"""
clock2.py
Created by: Eric Dean
Last updated: 12/12/23
Comment: Simulating the actual Constellation_Pass_Clock
"""
# Importing modules
from datetime import timezone,timedelta,datetime as dt
import warnings
import random
import pandas as pd
import streamlit as st
import time

# Disabling Future Warnings
warnings.simplefilter(action='ignore',category=FutureWarning)

# Creating Fake Data
# JDAY, AOS, LOS, SCID GND REV MAXE
global data
#now = dt.now(timezone.utc).replace(microsecond=0)
now = dt(2023,12,31,23,55,55)


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

    jday_data.append((now+d).timetuple().tm_yday) # new jday
    aos_data.append(now + d) # aos/los are currently full dts whereas in the emails its just a time
    los_data.append(now + d1)


data = []
for i in range(0,len(aos_data)):
    contact = [jday_data[i],aos_data[i],los_data[i],scid[i],gnd[i],ele[i]]
    # used to have jday = problematic when trying to use regular(actual) methodology
    data.append(contact)

def contact_schedule(num_contacts,scid_list,i):

    #new_now = dt.now(timezone.utc).replace(microsecond=0)
    #new_now = dt(new_now.year,new_now.month,new_now.day,\
    #             new_now.hour,new_now.minute,new_now.second) # aware -> naive
    new_now = now + timedelta(seconds=i)

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

            los_full_00 = dt.strptime(los_full_str,'%j %H:%M:%S') # defaults to 1900
            aos_full_00 = dt.strptime(aos_full_str,'%j %H:%M:%S')
            los_full_pres = dt(now.year,los_full_00.month,los_full_00.day,\
                               los_full_00.hour,los_full_00.minute,los_full_00.second)
            aos_full_pres = dt(now.year,aos_full_00.month,aos_full_00.day,\
                               aos_full_00.hour,aos_full_00.minute,aos_full_00.second)
            # Year Change Conditions
            # aos in 2023 but los in 2024 - good because now.year is used and the td would be negative =
                # caught by Jday Change Condition 
                # aos 2023-12-31 23:59:59
                # los 2023-1-1   00:00:01 -- result in negtive time diff (td temp is neg -> overwritten by jd_change!
            # since aos_full_pres uses now.year it will think is 01-01-2023 so it will be left out
            # if aos_pres.year == 2023 (now.year) & los_pres.year == 2023 (now.year) and \
            #  aos_pres.month == 1 and los_pres.month == 1 and now.month = 12:
            #   yr_change = now + time
                #

            # need to test
            # Year Change Condition - if aos & los are in 2024 but now is in 2023
            # Why not extract exact year from AOS - bc its not in the real data

            td_temp = (los_full_pres - aos_full_pres).total_seconds() # negative = day change
            
            # Year Change Condition
            if aos_full_pres.year == now.year and los_full_pres.year == now.year and\
               aos_full_pres.month == 1 and los_full_pres.month == 1 and now.month != 1:
                yr_change = now + timedelta(days=4)
                aos_full_pres = dt(yr_change.year,aos_full_00.month,aos_full_00.day,\
                                   aos_full_00.hour,aos_full_00.minute,aos_full_00.second)
                los_full_pres = dt(yr_change.year,los_full_00.month,los_full_00.day,\
                                   los_full_00.hour,los_full_00.minute,los_full_00.second)
             
            # Jday Change Condition - if aos & los are on different days
            if td_temp < 0:
                jd_change = now + timedelta(days=1)
                los_full_pres = dt(jd_change.year,jd_change.month,jd_change.day,\
                                   los_full_00.hour,los_full_00.minute,los_full_00.second)
            td_temp = (los_full_pres - aos_full_pres).total_seconds() # this wasn't here before!
        

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
        durf.append(int(dur[x]))
        act.append(flag[x])
        tl.append(str(td[x]))

    keys = ["SCID","AOS","LOS","Ground Site","Max Elevation","Duration","Active","Time Left"]
    vals = [scid,aos,los,gnd,ele,durf,act,tl]
    res = dict(zip(keys,vals))
    df = pd.DataFrame(res)
    return df[["SCID","AOS","LOS","Ground Site","Max Elevation","Duration","Active","Time Left"]]

# Coloring fn
thirty_secs = dt.strptime("00:00:30","%H:%M:%S")
def highlight_active(s):
    countdown_secs = dt.strptime(s[:][7],"%H:%M:%S")

    if s[:][6] == "\u2705" and countdown_secs > thirty_secs:
        return['background-color: #90EE90']*len(s)

    elif(s[:][6] == "\u2705") and countdown_secs <= thirty_secs and (thirty_secs - countdown_secs).total_seconds() % 2 != 0:
         return['background-color: yellow']*len(s)

    elif(s[:][6] == "\u274C" or s[:][6] == "\u2705") and \
        countdown_secs <= thirty_secs and \
        (thirty_secs - countdown_secs).total_seconds() % 2 == 0:
        return ['background-color: #90EE90']*len(s)
    
    elif(s[:][6]== "\u274C" or s[:][6] == "\u2705") and \
    countdown_secs <= thirty_secs and \
    (thirty_secs - countdown_secs).total_seconds() % 2 != 0:
        return ['background-color: yellow']*len(s)
    
    elif s[:][6] == "\u274C" and countdown_secs > thirty_secs:
        return ['background-color: yellow']*len(s)
    
# GUI Function
def gui():

    placeholder = st.empty()
    i = 0
    # using i to overwrite new now into a dt around the year change
    while True:

        with placeholder.container():
            scid_list = [1,2,3,4,5,6]
            num_contacts = 9
            df = contact_schedule(num_contacts,scid_list,i)
            if num_contacts == 0: # this is new put it in the presentation!!
                last8 = df.iloc[1:,:]
            else: # this is also new
                num_contacts -= 1
                last8 = df.iloc[-num_contacts:,:]

            st.caption("Closest Pass")
            kpi1,kpi2,kpi3,kpi4,kpi5,kpi6,kpi7,kpi8 = st.columns(8)
            next = df.iloc[0,:]

            kpi1.metric(label = "SCID \U0001F6F8", value = next.iloc[0])
            kpi2.metric(label = "AOS \u231B", value = str(next.iloc[1]))
            kpi3.metric(label = "LOS \u23F3 ", value = str(next.iloc[2]))
            kpi4.metric(label = "Ground Site \U0001F4E1", value = next.iloc[3])
            kpi5.metric(label = "Max Elevation [deg] \u26F0", value = next.iloc[4])
            kpi6.metric(label = "Duration [s] \u23F1", value = next.iloc[5])
            kpi7.metric(label = "Active \u2753", value = next.iloc[6])
            kpi8.metric(label = "Time Left \U0001F6D1", value = next.iloc[7])

            st.dataframe(last8.style.apply(highlight_active,axis=1))
            st.caption("\U0001F7E9 Active \U0001F7E8 Upcoming, The colors will alternate withing 30 seconds of AOS & LOS.")
            i += 1
            time.sleep(1)

if __name__ == '__main__':

    # Page config
    st.set_page_config(
        page_title= 'Constellation Pass Clock',
        page_icon = '\u23F0',
        layout='wide'
    )
    st.title("Constellation Pass Clock \u23F0")

    gui()
