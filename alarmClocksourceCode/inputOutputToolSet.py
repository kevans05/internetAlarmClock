__author__ = 'kevans05'
import Adafruit_BBIO.UART as UART
import serial

class inputFromPIC:
    def setUPBBUART(self):
        UART.setup("UART1")

    def readInputOutput(self):
            ser = serial.Serial(port = "/dev/ttyO1", baudrate=115200)
            return ser.read
    def makeDecisions(self):

        if readInputOutput() == 0:
            print "win"

