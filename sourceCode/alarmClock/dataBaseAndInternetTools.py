__author__ = 'kevans05'
import dataset
import urllib2

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
                os.system('sh ./shellScripts/setRealTimeClock.sh')
            else:
                print "Hardware TIME:", strftime("%I:%M:%S", localtime())
        else:
            print "NTP CHECK FAILED \n\n Hardware TIME:", strftime("%I:%M:%S", localtime())



class dataBaseTools:
    def pullDB(self):
        #db = dataset.connect('mysql://root:root@localhost/test') #Use if mySQL is implemented on machine
        db = dataset.connect('sqlite:///alarmClock.db') #Use if no mySQL on system
        alarmTable = db['alarm']
        return db
