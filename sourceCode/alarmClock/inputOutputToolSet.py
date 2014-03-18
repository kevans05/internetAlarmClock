__author__ = 'kevans05'
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from Adafruit_BBIO.SPI import SPI


class volumeShit:
    currentVolume = 10
    #class: voulumeIncrease
    #created by: Kyle Evans
    #Description: changes the pwm of what is being applies to the bwm port on the sound chip
    def voulumeIncrease(self):
        if currentVolume < 100:
            currentVolume = 100
        else:
            currentVolume += 1
        PWM.set_duty_cycle("P9_14", currentVolume)
    #class: volumeDecrease
    #created by: Kyle Evans
    #Description: changes the pwm of what is being applies to the bwm port on the sound chip
    def volumeDecrease(self):
        currentVolume -= 1
        PWM.set_duty_cycle("P9_14", currentVolume)
    #class: muteVolume
    #created by: Kyle Evans
    #Description: changes the pwm of what is being applies to the bwm port on the sound chip
    def muteVolume(self):
        currentVolume = 0
        PWM.stop("P9_14")
        PWM.cleanup()
    #class: volumeIntuate
    #created by: Kyle Evans
    #Description: changes the pwm so it can start at a good level
    def volumeIntuate(self):
        PWM.start("P9_14", 50)
#class: switches
#created by: Kyle Evans
#Description: initializes the SPI
class switches:
    def initializeMCP3008(self):
        global SPICLK = 18
        global SPIMISO = 23
        global SPIMOSI = 24
        global SPICS = 25
        global buttonInputADC = 0;

        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)

        buttenPressed = 0

    #ok so we are going with my ADC resister value plan. This mensa each button will have its own resistor
    def readADC(adcnum, clockpin, mosipin, misopin, cspin):
        # there are 7 channels on the adc if it returns a value that is greater then 7 or less then 0 it returns a error
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)

        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
    def scanningForInput(self):
        # we'll assume that there is no buttonInput didn't move
        buttonInputChanged = False

        # read the analog pin
        currentButtonValue = readadc(buttonInputADC, SPICLK, SPIMOSI, SPIMISO, SPICS)
        # how much has it changed since the last read?
        pot_adjust = abs(currentButtonValue - last_read)

        if DEBUG:
                print "currentButtonValue:", currentButtonValue
                print "pot_adjust:", pot_adjust
                print "last_read", last_read

        if ( pot_adjust > tolerance ):
               buttonInputChanged = True

        if DEBUG:
                print "buttonInputChanged", buttonInputChanged

        if ( buttonInputChanged ):

                last_read = trim_pot

    def whatToDo(buttonValue):
        choices = {1:'one', 2:'two'}
        try:
            print choices[buttonValue]
        except KeyError:
            return -1