import ntplib,datetime, os, urllib2
from time import ctime, localtime, strftime,sleep


def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def compairNTPvsOS():
	if internet_on() == True:
		c = ntplib.NTPClient()
		response = c.request('0.ca.pool.ntp.org', version=3)
		if(abs(response.offset) >= 60):
			print "NTP TIME:", ctime(response.tx_time)
			os.system('sh ./setRealTimeClock.sh')
		else:
			print "Hardware TIME:", strftime("%I:%M:%S", localtime())
	else:
		print "NTP CHECK FAILED \n\n Hardware TIME:", strftime("%I:%M:%S", localtime())ß

def checkAlarm():
	print "I need an alarm function"


def main():
	compairNTPvsOS()
	var = 0
	os.system('clear') 
	while True:
		if var >= 3600:
			var = 0
			compairNTPvsOS
		else:
			checkAlarm()
			print var
		var+=1
		sleep(1)
		os.system('clear') 

main()


