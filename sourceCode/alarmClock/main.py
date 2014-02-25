__author__ = 'Kyle Evans'
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.floatlayout import FloatLayout
from math import cos, sin, pi
from kivy.lang import Builder
from kivy.properties import NumericProperty
from time import ctime, localtime, strftime, sleep

import dataset, urllib2, webbrowser,datetime,os

class ClockTools(Label):
    def update(self, *args):
        self.font_size = '100dp'
        self.halign = 'left'
        self.padding_y = 175
        self.text = strftime("%I:%M:%S %p", localtime()) + "\n" + strftime("%d-%B-%Y", localtime())

kv = '''
#:import math math

[ClockNumber@Label]:
    text: str(ctx.i)
    pos_hint: {"center_x": 0.5+0.42*math.sin(math.pi/6*(ctx.i-12)), "center_y": 0.5+0.42*math.cos(math.pi/6*(ctx.i-12))}
    font_size: self.height/16

<MyClockWidget>:
    face: face
    ticks: ticks
    FloatLayout:
        id: face
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: 0.9*min(root.size), 0.9*min(root.size)
        canvas:
            Color:
                rgb: 0.1, 0.1, 0.1
            Ellipse:
                size: self.size
                pos: self.pos
        ClockNumber:
            i: 1
        ClockNumber:
            i: 2
        ClockNumber:
            i: 3
        ClockNumber:
            i: 4
        ClockNumber:
            i: 5
        ClockNumber:
            i: 6
        ClockNumber:
            i: 7
        ClockNumber:
            i: 8
        ClockNumber:
            i: 9
        ClockNumber:
            i: 10
        ClockNumber:
            i: 11
        ClockNumber:
            i: 12
    Ticks:
        id: ticks
        r: min(root.size)*0.9/2
'''
Builder.load_string(kv)

class MyClockWidget(FloatLayout):
    pass

class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            Color(0.2, 0.5, 0.2)
            Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            Color(0.3, 0.6, 0.3)
            Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")

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
                os.system('sh ./setRealTimeClock.sh')
            else:
                print "Hardware TIME:", strftime("%I:%M:%S", localtime())
        else:
            print "NTP CHECK FAILED \n\n Hardware TIME:", strftime("%I:%M:%S", localtime())

class alarmTools:
    def checkAlarm(self):
        dataBaseSet = dataBaseTools()
        dbFile = dataBaseSet.pullDB()
        internetToolSet = internetTools()
        now = localtime()
        alarmTable = dbFile['alarm']
        nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
        if nextAlarm != None:
            if internetToolSet.internetOn() == True and nextAlarm.items()[7][1] != True:
                value = nextAlarm.items()[6][1]
                idtoChange = nextAlarm.items()[0][1]
                nextAlarm = dict(id=idtoChange, alarmTriggered=True)
                alarmTable.update(nextAlarm, ['id'])
                webbrowser.open(value)
            else:
			    cycles = 0
			    while cycles <= 10:
				    os.system('say "WAKE THE FUCK UP"')
				    cycles+=1
    def goToSleep(self):
        dataBaseSet = dataBaseTools()
        dbFile = dataBaseSet.pullDB()
        internetToolSet = internetTools()
        now = localtime()
        alarmTable = dbFile['alarm']
        nextAlarm = alarmTable.find_one(year=now.tm_year,month=now.tm_mon,day=now.tm_mday,hour=now.tm_hour,minute=now.tm_min)
        if now.tm_min < 54:
            minuteValue = ((now.tm_min - 60)+5)
            hourValue = (now.tm_hour + 1)
        else:
            minuteValue = 5+tm_min
            hourValue = (now.tm_hour)

        if nextAlarm != None:
                value = nextAlarm.items()[6][1]
                idtoChange = nextAlarm.items()[0][1]
                nextAlarm = dict(id=idtoChange,hour=hourValue, minute=minuteValue)
                alarmTable.update(nextAlarm, ['id'])


class dataBaseTools:
    def pullDB(self):
        #db = dataset.connect('mysql://root:root@localhost/test') #Use if mySQL is implemented on machine
        db = dataset.connect('sqlite:///alarmClock.db') #Use if no mySQL on system
        alarmTable = db['alarm']
        return db

class TimeApp(App):
    def build(self):
        analogDigital = True
        #analogDigital = False
        alarm = alarmTools
        Clock.schedule_interval(alarm.checkAlarm, 1)
        Clock.schedule_interval(alarm.checkAlarm, 1)
        if(analogDigital == True):
            clockGUI = ClockTools()
            Clock.schedule_interval(clockGUI.update, 1)
            return clockGUI
        elif(analogDigital != True):
            clockGUI = MyClockWidget()
            Clock.schedule_interval(clockGUI.ticks.update_clock, 1)
            return clockGUI


class volumeShit:
    currentVolume = 10
    def voulumeIncrease(self):
        if currentVolume =< 100:
            currentVolume = 100
        else:
            currentVolume += 1
        PWM.set_duty_cycle("P9_14", currentVolume)

    def volumeDecrease(self):
        currentVolume -= 1
        PWM.set_duty_cycle("P9_14", currentVolume)

    def muteVolume(self):
        currentVolume = 0
        PWM.stop("P9_14")
        PWM.cleanup()

    def volumeControl(self):
        if inputBefore > inputAfter:
            volumeDecrease
        elif inputBefore < inputAfter:
            voulumeIncrease
        elif currentVolume >= 0:
            muteVolume

    def volumeIntuate(self):
        PWM.start("P9_14", 50)
class switches:
    # this is the plan http://arduino.cc/en/Tutorial/Debounce#.UwwbOPldWJE maybe go a little deeper but fuck it this will work
    lastButtonState
    lastDebounceTime
    buttonState
    #I will pass in the pinThatisBeingCalled in this one so i can reuse
    def switchDebouncing(self,pinNumber):
        reading = GPIO.wait_for_edge(pinNumber, GPIO.RISING)
        if reading != lastButtonState:
            lastDebounceTime = time.time() * 1000

        if ((time.time() * 1000)-lastDebounceTime) > debounceDelay:
            if reading != buttonState:
                buttonState = reading
                if buttonState == True:
                    return True
    #same thing gose here
    def switchSetUp(self, pinNumber):
        #call the pin and set its standard state
        GPIO.output(pinNumber, GPIO.HIGH)
        GPIO.cleanup()

if __name__ == "__main__":
    TimeApp().run()