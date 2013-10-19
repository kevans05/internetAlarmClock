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
	#print "Next Alarm", alarmTimeData
	#if now == alarmTimeData:
		#webbrowser.open(webAddress)
def pullCSV():
	TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	with open('egg.csv', 'rU') as csvfile:
		return csvfile

		#spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		#rownum = 0
		#try:
		#	for row in spamreader:
		#		if(rownum == 1):
		#			alarmTimeData = datetime.datetime.strptime(row[0], '%m/%d/%Y/%H:%M')
		#			print alarmTimeData
		#		elif(rownum == 2):
		#			webAddress = row[0]
		#			print webAddress
		#		rownum += 1
		#except csv.Error as e:
		#	sys.exit()
def getTimeFromCSV(csvfile):
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	rownum = 0
	try:
		for row in spamreader:
			if(rownum == 1):
				return datetime.datetime.strptime(row[0], '%m/%d/%Y/%H:%M')
			else:
				return Error
			rownum+=rownum
	except Exception, e:
		raise e
		return Error

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
			csvFile = pullCSV()
			getTimeFromCSV(csvFile)
		else:
			checkAlarm(now)
			y = strftime("%H:%M:%S", localtime())
			print "True time:", y#, "Alarm Off:", alarm_HH, alarm_MIN 
			#print var
		var+=1
		sleep(1)
		os.system('clear') 

main()


