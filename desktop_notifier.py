import time

import plyer
import requests
from plyer import *
import datetime

EEECS_data = None

try:
    EEECS_data = "link to EEECS Api data"
except:
    print('Internet Error; Check your connection')

if (EEECS_data != None):
    E_data = EEECS_data.json()['Success']

    while True:
        plyer.notification.notify(
            notification_title = "Alerts from EEECS QUB website on {}".format(datetime.date.today()),
            alert = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = E_data['cases'],
                        todaycases = E_data['todayCases'],
                        todaydeaths = E_data['todayDeaths'],
                        active = E_data["active"]),
            app_icon = "", #download app icon of ico format
            timeout = 50
        )
        #set the number of hours to stay dormant before checking for notification again
        time.sleep(60*60*1) #sleep for 1 hour


# updated EEECS_notify
#
# to build an api later for data ==> QUB EEECS website