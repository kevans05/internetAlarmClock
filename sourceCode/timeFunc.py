import ntplib,datetime
from time import ctime


def compairNTPvsOS():
	c = ntplib.NTPClient()
	response = c.request('europe.pool.ntp.org', version=3)
	response.offset

compairNTPvsOS( );


