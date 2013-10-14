import ntplib,datetime, os, urllib2, csv, webbrowser
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


def checkAlarm(now):
	print "I need an alarm function"
	#if(now.tm_hour == int(alarm_HH)):
	#	webbrowser.open(webAddress)

def pullOnCSV():
	ifile  = open('egg.csv', "rb")
	spamreader = csv.reader(ifile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print ', '.join(row)
	sleep(5)

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
			pullOnCSV()
		else:
			checkAlarm(now)
			y = strftime("%H:%M:%S", localtime())
			print "True time:", y#, "Alarm Off:", alarm_HH, alarm_MIN 
			#print var
		var+=1
		sleep(1)
		os.system('clear') 

main()


