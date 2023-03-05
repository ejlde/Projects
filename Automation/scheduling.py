import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime

# @repeat(every(5).seconds) # annotation so that commands aren't needed
##
# Running Schedule
#def job():
   # print("Food is good")

#schedule.every(5).seconds.do(job)

##
# Schedule every day
#schedule.every().day.at("18:52").do(job)

# every minute at forty seconds
#schedule.every().minute.at(":40").do(job)

##
# Schedule Limits
# every hour until 8 hrs have passed
# schedule.every().hour.until(timedelta(hours=8)).do(job)

# every hour until specific time
# schedule.every().hour.until(time(11,33,42)).do(job)

# Rand 1-5 do job 
# schedule.every(1).to(5).seconds.do(job)

##
# Cancel Job
#j = schedule.every(1).to(5).seconds.do(job)
#counter= 0

##
# Annotations
# Automating reminders
# @repeat(every(5).seconds,message="Subscribe") # annotation so that commands aren't needed
# @repeat(every(2).seconds,message="Hey")

# def job(message):
#     print("Hello the message is:",message)

# with annotation
#@repeat(every(30).minutes)
def break_reminder():
    print("Take a break! You have been working for 30 minutes")

schedule.every().day.at("10:00").do(break_reminder)

while True:
    schedule.run_pending()
    tm.sleep(1)
    
    #counter += 1 # increased every second
    #if counter == 10:
     #   schedule.cancel_job(j)


