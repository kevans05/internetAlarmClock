from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

from time import ctime, localtime, strftime, sleep

import ntplib,datetime, os, urllib2, webbrowser, dataset, thread

class internetTools():
    def internetOn(self):
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False

    def compairNTPvsOS(self):
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

class testTools:
	def testTheDataBase(self,db):
		for alarm in db['alarm']:
			print alarm['day'], alarm['hour'], alarm['minute']
	def printOutColumnTitals(slef,db):
		print(db['alarm'].columns)

class dataBaseTools:                   
    def pullDB(self, now):
        #db = dataset.connect('mysql://root:root@localhost/test') ##Use if mySQL is implemented on machine
        db = dataset.connect('sqlite:///alarmClock.db') ##Use if no mySQL on system
        alarmTable = db['alarm']
        return db

class alarmTools:
    def checkAlarm(self, now, dbFile):
    	internetToolSet = internetTools()
        alarmTable = dbFile['alarm']
        nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
        if nextAlarm != None:
        	if internetToolSet.internetOn() == True:
        		print nextAlarm 
	            #webbrowser.open(nextAlarm.webaddress)
	        else:
	            cycles = 0
	            while cycles <= 10:
	                os.system('say "WAKE THE FUCK UP"')
	                cycles+=1
       	else:
       		print "noAlarm"

class InPutOutPutTools:
	def volumeControl(self):
		return 0

class timeDisplay(Label):
    def update(self, *args):
    	##Set the font size in pixles
    	self.font_size = '100dp'
    	## alighns the text to the left hand side of the screen
    	self.halign = 'left'
    	#self.color=[0, 0, 8, 1]
    	## changes the top of the Y corrdanit acotidnig the the walls
    	self.padding_y = 175
    	##displays the Text east as shit to change considering pulling in the time so I can ensure it is correct to alarm just incase something gose wrong
        self.text = strftime("%I:%M:%S %p", localtime()) + "\n" + strftime("%d-%B-%Y", localtime())

class main(App):
	def build(self):
		##Creats a database toolset to be used in the main
		dataBaseSet = dataBaseTools()
		##this is a toolset I built so I can test my thinking i creat it
		testToolSet = testTools()
		#creats the alarm tools
		alarmToolSet = alarmTools()
		#this is the display
		clockGUI = timeDisplay()
		##call the current Time fuction and assigne it to current time
		currentTime = localtime()


		## I call the current database and asign it to the dbFile
		dbFile = dataBaseSet.pullDB(currentTime)
		##I am using the tool set so that I can swee what is in the database
		testToolSet.printOutColumnTitals(dbFile)
		## should call the alarm but is not currently working
		##Is the GUI that displays the time
        time.ctime(alarmToolSet.checkAlarm(currentTime,dbFile))
		Clock.schedule_interval(clockGUI.update, 1)
		return clockGUI


if __name__ == "__main__":
    main().run()