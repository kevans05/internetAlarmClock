import dataset, time, os,signal
from selenium import webdriver

def alarmChannelLookUp(newAlarmchannel):
	preSet = dbFile['preSetTable']
	if(newAlarmchannel > 7):
		return 'http://www.youtube.com/watch?v=0mZdhHG5ZCA&feature=share&list=PL084E6F640B3B0A55'
	else:
		return alarmTable.find_one(id=newAlarmchannel)

def addNewAlarm(newAlarmYear, newAlarmmounth, newAlarmday, newAlarmhour, newAlarmmin, newAlarmchannel):
	now = localtime()
	alarmTable = dbFile['alarm']
	if newAlarmYear>=now.tm_year:
		if newAlarmmounth>=now.tm_mon:
			if newAlarmday>=now.tm_mday:
				if newAlarmhour>=now.tm_hour:
					if newAlarmmin>=now.tm_min:
						nextAlarm = alarmTable.insert(year=newAlarmYear,month=newAlarmmounth,day=newAlarmday,hour=newAlarmhour,minute=newAlarmmin,webaddress=alarmChannelLookUp(newAlarmchannel))

def stopAlarm(browser):
	browser.quit()

def sleepPressed():
	


def main():
	#browser = webdriver.Firefox()
	#browser.get('http://www.youtube.com/watch?v=0mZdhHG5ZCA&feature=share&list=PL084E6F640B3B0A55')
	#time.sleep(10)
	#stopAlarm(browser)


main()


