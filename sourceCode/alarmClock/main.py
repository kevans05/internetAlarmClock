__author__ = 'Kyle Evans'
#Parts of KIVY that the main uses. I had to make a seprate GUI file becouse it was getting a little out of control in here
from kivy.app import App
from kivy.clock import Clock
from time import ctime, localtime, sleep
#Imports of files that I created are called here
from GUITools import *
from dataBaseAndInternetTools import *


import webbrowser,datetime,os

class alarmTools:
    def checkAlarm(self):
        dataBaseSet = dataBaseTools()
        dbFile = dataBaseSet.pullDB()
        internetToolSet = internetTools()
        now = localtime()
        alarmTable = dbFile['alarm']
        nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
        if nextAlarm != None:
            if internetToolSet.internetOn() == True and nextAlarm.items()[7][1] != True:
                os.system("TASKKILL /F /IM firefox")
                value = nextAlarm.items()[6][1]
                idtoChange = nextAlarm.items()[0][1]

                nextAlarm = dict(id=idtoChange, alarmTriggered=True)
                alarmTable.update(nextAlarm, ['id'])
                webbrowser.open(value)
            else:
                cycles = 0
                while cycles <= 10:
                    os.system('say "WAKE THE FUCK UP"')
                    cycles+=1
    def goToSleep(self):
        dataBaseSet = dataBaseTools()
        dbFile = dataBaseSet.pullDB()
        internetToolSet = internetTools()
        now = localtime()
        alarmTable = dbFile['alarm']
        nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
        if now.tm_min < 54:
            minuteValue = ((now.tm_min - 60)+5)
            hourValue = (now.tm_hour + 1)
        else:
            minuteValue = 5+tm_min
            hourValue = (now.tm_hour)

        if nextAlarm != None:
                value = nextAlarm.items()[6][1]
                idtoChange = nextAlarm.items()[0][1]
                nextAlarm = dict(id=idtoChange,hour=hourValue, minute=minuteValue)
                alarmTable.update(nextAlarm, ['id'])

class TimeApp(App):
    def build(self):

        analogDigital = True
        #analogDigital = False
        internetToolSet = internetTools()
        alarm = alarmTools
        Clock.schedule_interval(alarm.checkAlarm, 1)
        Clock.schedule_interval(internetToolSet.compairNTPvsOS, 1)
        if(analogDigital == True):
            clockGUI = ClockTools()
            Clock.schedule_interval(clockGUI.update, 1)
            return clockGUI
        elif(analogDigital != True):
            clockGUI = MyClockWidget()
            Clock.schedule_interval(clockGUI.ticks.update_clock, 1)
            return clockGUI

if __name__ == "__main__":
    TimeApp().run()