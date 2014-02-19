import dataset
from time import localtime

def main():
	now = localtime()

	db = dataset.connect('sqlite:///alarmClock.db') ##Use if no mySQL on system
	alarmTable = db['alarm']
	alarmTable.insert(dict(alarmTriggered = False, alarmName = "testing",year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=(now.tm_min+1) , webaddress="http://www.youtube.com/watch?v=5y_KJAg8bHI"  ))
	print "I ran"

main()