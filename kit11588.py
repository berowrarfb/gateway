import RPi.GPIO as GPIO
import time

# init
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init pins
pin_led_blue = 18
pin_led_red = 23
pin_led_green = 24

GPIO.setup(pin_led_blue,GPIO.OUT)
GPIO.setup(pin_led_red,GPIO.OUT)
GPIO.setup(pin_led_green,GPIO.OUT)


print("LED on")
GPIO.output(pin_led_blue,GPIO.HIGH)
GPIO.output(pin_led_red,GPIO.HIGH)
GPIO.output(pin_led_green,GPIO.HIGH)


time.sleep(1)

print("LED off")
GPIO.output(pin_led_blue,GPIO.LOW)
GPIO.output(pin_led_red,GPIO.LOW)
GPIO.output(pin_led_green,GPIO.LOW)

class led_breakout_kit11588():
    '''
    '''

    status = {'red' : False, 'green' : False, 'blue' : False}

    # init pins
    _pin_led_blue = 18
    _pin_led_red = 23
    _pin_led_green = 24
	
    def __init__(self, status=status):
	self.status = status

    def get_status(self):
	'''
	'''
	return self.status

    # def led_on(self, colour):
    #     '''
    #     '''
    #     if colour == 'red':
