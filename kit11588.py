import RPi.GPIO as GPIO
import time

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
        self.on_activate()
        self.set_led({'all':False})
	
    def on_activate(self):
        ''' Init the device hardware
        '''
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
	
        GPIO.setup(self._pin_led_blue, GPIO.OUT)
        GPIO.setup(self._pin_led_red, GPIO.OUT)
        GPIO.setup(self._pin_led_green, GPIO.OUT)

    def get_status(self):
        ''' Return the status dict of the LEDs
        '''
        return self.status

    def set_led(self, new_status_dict):
        ''' Update the LED status dict
        '''
        for colour in new_status_dict:
            if colour == 'red':
                if new_status_dict[colour] is True:
                    GPIO.output(self._pin_led_red, GPIO.HIGH)
                    self.status['red'] = True
                else:
                    GPIO.output(self._pin_led_red, GPIO.LOW)
                    self.status['red'] = False
		    
            elif colour == 'green':
                if new_status_dict[colour] is True:
                    GPIO.output(self._pin_led_green, GPIO.HIGH)
                    self.status['green'] = True
                else:
                    GPIO.output(self._pin_led_green, GPIO.LOW)
                    self.status['green'] = False
		    
            elif colour == 'blue':
                if new_status_dict[colour] is True:
                    GPIO.output(self._pin_led_blue, GPIO.HIGH)
                    self.status['blue'] = True
                else:
                    GPIO.output(self._pin_led_blue, GPIO.LOW)
                    self.status['blue'] = False
            elif colour == 'all':
                if new_status_dict[colour] is True:
                    GPIO.output(self._pin_led_red, GPIO.HIGH)
                    GPIO.output(self._pin_led_green, GPIO.HIGH)
                    GPIO.output(self._pin_led_blue, GPIO.HIGH)
                else:
                    GPIO.output(self._pin_led_red, GPIO.LOW)
                    GPIO.output(self._pin_led_green, GPIO.LOW)
                    GPIO.output(self._pin_led_blue, GPIO.LOW)
