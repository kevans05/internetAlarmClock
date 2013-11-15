import ntplib,datetime, os, urllib2, webbrowser, dataset
from time import ctime, localtime, strftime,sleep

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


def checkAlarm(now, dbFile):
	print "I need an alarm function"
	alarmTable = dbFile['alarm']
	nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
	if nextAlarm != None:
		webbrowser.open(nextAlarm.webaddress)
def pullDB():
	db = dataset.connect('sqlite:///alarmClock.db')
	alarmTable = db['alarm']
	return db
def main():
	compairNTPvsOS()
	var = 0
	os.system('clear') 
	while True:
		now = localtime()
		if var >= 3600:
			var = 0
			compairNTPvsOS
		elif  var%60 == 0:
			dbFile = pullDB()
		else:
			checkAlarm(now, dbFile)
			y = strftime("%H:%M:%S", localtime())
			print "True time:", y#, "Alarm Off:", alarm_HH, alarm_MIN 
			#print var
		var+=1
		sleep(1)
		os.system('clear') 

main()


