__author__ = 'kevans05'
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

class volumeShit:
    currentVolume = 10
    def voulumeIncrease(self):
        if currentVolume < 100:
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
    lastButtonState = False
    lastDebounceTime = False
    buttonState = False
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
