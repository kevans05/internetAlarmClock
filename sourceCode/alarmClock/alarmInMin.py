import dataset
from time import localtime

def main():
	now = localtime()
	x =0
	db = dataset.connect('sqlite:///alarmClock.db') ##Use if no mySQL on system
	alarmTable = db['alarm']
	while x is not 60:
		alarmTable.insert(dict(alarmTriggered = False, alarmName = "testing",year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=x , webaddress="http://www.youtube.com/watch?v=5y_KJAg8bHI"  ))
		x+=1
	print "I ran" 
main()