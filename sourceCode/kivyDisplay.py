from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from time import ctime, localtime, strftime,sleep
import ntplib,datetime, os, urllib2, webbrowser, dataset, thread


class internetTools():
    def internetOn():
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False

    def compairNTPvsOS():
        if internetOn() == True: 
            c = ntplib.NTPClient()
            response = c.request('0.ca.pool.ntp.org', version=3)
            if(abs(response.offset) >= 60):
                print "NTP TIME:", ctime(response.tx_time)
                os.system('sh ./setRealTimeClock.sh')
            else:
                print "Hardware TIME:", strftime("%I:%M:%S", localtime())
        else:
            print "NTP CHECK FAILED \n\n Hardware TIME:", strftime("%I:%M:%S", localtime())

class alarmClass():
    def checkAlarm(now, dbFile, *args):
        alarmTable = dbFile['alarm']
        nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
        if nextAlarm != None and nextAlarm.alarmTriggered != 1:
            if internetOn() == True: 
                webbrowser.open(nextAlarm.webaddress)
            else:
                cycles = 0
                while cycles <= 10:
                    os.system('say "WAKE THE FUCK UP"')
                    cycles+=1

class dataBaseTool():                   
    def pullDB(now, *args):
        #db = dataset.connect('mysql://root:root@localhost/test') ##Use if mySQL is implemented on machine
        db = dataset.connect('sqlite:///alarmClock.db') ##Use if no mySQL on system
        alarmTable = db['alarm']
        return db


class timeDisplay(Label):
    def update(self, *args):
    	self.font_size = '100dp'
    	self.halign = 'left'
    	#self.color=[0, 0, 8, 1]
    	self.padding_y = 175
        self.text = strftime("%I:%M:%S %p", localtime()) + "\n" + strftime("%d-%B-%Y", localtime())

class main(App):
    def build(self):
        currentTime = localtime()
        clock = timeDisplay()
        database = dataBaseTool()
        alarm = alarmClass()
        dbFile=database.pullDB(currentTime)

        alarm.checkAlarm(currentTime,dbFile)

        Clock.schedule_interval(clock.update, 1)
        return clock

if __name__ == "__main__":
    main().run()

