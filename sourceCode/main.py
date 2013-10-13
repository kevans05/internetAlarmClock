import ntplib,datetime
from time import ctime


def main():




if __name__ == "__main__":
main()


def compairNTPvsOS():
	c = ntplib.NTPClient()
	response = c.request('europe.pool.ntp.org', version=3)
	if response.offset >= 60:
		print "NTP TIME:", c
	else
		print "Hardware TIME:",datetime.now()


compairNTPvsOS( );

