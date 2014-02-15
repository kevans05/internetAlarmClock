import ntplib,datetime, os, urllib2, webbrowser, dataset, thread
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
	alarmTable = dbFile['alarm']
	nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
	if nextAlarm != None and nextAlarm.alarmTriggered != True:
		if internetOn() == True: 
			webbrowser.open(nextAlarm.webaddress)
		else:
			cycles = 0
			while cycles <= 10:
				os.system('say "WAKE THE FUCK UP"')
				cycles+=1

def pullDB(now):
	#db = dataset.connect('mysql://root:root@localhost/test') ##Use if mySQL is implemented on machine
    db = dataset.connect('sqlite:///alarmClock.db') ##Use if no mySQL on system
    alarmTable = db['alarm']
    #if(db['alarm'].columns == "set([u'webaddress', u'hour', u'id', u'alarmTriggered', u'alarmName', u'month', u'day', u'minute'])" is False):
    alarmTable.insert(dict(alarmName = 'system boot', year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min,webaddress='http://www.youtube.com/watch?v=T4nLjWqfiZ4', alarmTriggered = True))
    #	print "preloadedID FAIL NEW GENERATION"
    #else:
    	#print "preloadedID"
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
			dbFile = pullDB(now)
		else:
			checkAlarm(now, dbFile)
			y = strftime("%H:%M:%S", localtime())
			print "True time:", y
		var+=1
		sleep(1)
		os.system('clear') 

main()


