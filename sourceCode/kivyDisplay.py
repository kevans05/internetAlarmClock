from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

from time import ctime, localtime, strftime,sleep

class timeDisplay(Label):
    def update(self, *args):
    	self.font_size = '100dp'
    	self.halign = 'left'
    	#self.color=[0, 0, 8, 1]
    	self.padding_y = 175
        self.text = strftime("%I:%M:%S %p", localtime()) + "\n" + strftime("%d-%B-%Y", localtime())

class TimeApp(App):
    def build(self):
        crudeclock = timeDisplay()
        Clock.schedule_interval(crudeclock.update, 1)
        return crudeclock
class alarmFunction():
	d
if __name__ == "__main__":
    TimeApp().run()