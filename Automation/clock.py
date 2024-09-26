
# Importing modules
from datetime import timezone,timedelta,datetime as dt
import warnings
import random
import pandas as pd
import streamlit as st
import time

warnings.simplefilter(action='ignore',category=FutureWarning)

# Creating Fake Data
# JDAY, AOS, LOS, SCID GND REV MAXE
global data 
now = dt.now(timezone.utc).replace(microsecond=0)


jday = now.timetuple().tm_yday



aos_data = []
los_data = []
jday_data = []
scid = [1,2,3,4,5,6,\
        6,2,3,1,5,4,\
        1,2,3,4,5,6]
gnd = ['DEN','LA','SYD','LON','LA','DEN',\
       'SYD','LON','LON','DEN','LA','SYD',\
        'SYD','LON','DEN','LA','LA','DEN']
#rev = [1,1,1,1,1,1,1,1,1,1,1,1]
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

def contact_schedule(num_contacts,scid_list):

    new_now = dt.now(timezone.utc).replace(microsecond=0)

    # Finding upcoming & active contacts
    data_final = []
    for x in range(len(data)):
        contact_los = data[x][2]
        contact_jday = data[x][0]
        contact_scid = data[x][3]
        if contact_scid in scid_list:
            if(contact_jday == jday and contact_los.time() >= new_now.time()):
                data_final.append(data[x])
            elif(contact_jday > jday):
                data_final.append(data[x])

    # Finding the time difference between the contacts and now
    td = []
    flag = []
    dur = []
    for x in range(num_contacts):
        aos_final = data_final[x][1]
        los_final = data_final[x][2]

        if (aos_final > new_now):
            td.append(aos_final - new_now)
            flag.append("\u274C") # x emoji
            dur.append(int((los_final-aos_final).total_seconds()))

        elif(aos_final <= new_now and los_final >= new_now):
            flag.append("\u2705") # green check emoji
            td.append(los_final - new_now)
            dur.append(int((los_final-aos_final).total_seconds()))
    
    aos = []
    los = []
    scid = []
    gnd = []
    ele = []
    act = []
    tl = [] 
    for x in range(num_contacts):
        aos.append(data_final[x][1].time())
        los.append(data_final[x][2].time())
        scid.append(data_final[x][3])
        gnd.append(data_final[x][4])
        ele.append("{0:.1f}".format(data_final[x][5]))
        act.append(flag[x])
        tl.append(str(td[x]))

    keys = ["SCID","AOS","LOS","Ground Site","Max Elevation","Duration","Active","Time Left"]
    vals = [scid,aos,los,gnd,ele,dur,act,tl]
    res = dict(zip(keys,vals))
    df = pd.DataFrame(res)
    return df[["SCID","AOS","LOS","Ground Site","Max Elevation","Duration","Active","Time Left"]]
        
# Testing the fn
#out = contact_schedule(data_gen(),8)
#print(out)


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

    while True:

        with placeholder.container():
            scid_list = [1,2,3,4,5,6]
            num_contacts = 9
            df = contact_schedule(num_contacts,scid_list)
            last8 = df.iloc[-8:,:]

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
            time.sleep(0.1)

if __name__ == '__main__':

    # Page config
    st.set_page_config(
        page_title= 'Constellation Pass Clock',
        page_icon = '\u23F0',
        layout='wide'
    )
    st.title("Constellation Pass Clock \u23F0")

    gui()