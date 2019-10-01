# Demo of reading the range and lux from the VL6180x distance sensor and
# printing it every second.
# Author: Tony DiCola

 
 
# Create I2C bus.
#i2c = busio.I2C(board.SCL, board.SDA)
 
# Create sensor instance.
#sensor = adafruit_vl6180x.VL6180X(i2c)
 
# Main loop prints the range and lux every second:
#while True:
#    # Read the range in millimeters and print it.
#    range_mm = sensor.range
#    print('Range: {0}mm'.format(range_mm))
    # Read the light, note this requires specifying a gain value:
    # - adafruit_vl6180x.ALS_GAIN_1 = 1x
    # - adafruit_vl6180x.ALS_GAIN_1_25 = 1.25x
    # - adafruit_vl6180x.ALS_GAIN_1_67 = 1.67x
    # - adafruit_vl6180x.ALS_GAIN_2_5 = 2.5x
    # - adafruit_vl6180x.ALS_GAIN_5 = 5x
    # - adafruit_vl6180x.ALS_GAIN_10 = 10x
    # - adafruit_vl6180x.ALS_GAIN_20 = 20x
    # - adafruit_vl6180x.ALS_GAIN_40 = 40x
#    light_lux = sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)
#    print('Light (1x gain): {0}lux'.format(light_lux))
    # Delay for a second.
#    time.sleep(1.0)

import board
import busio
import adafruit_vl6180x

import adafruit_vl6180x

class sensor_vl6180x():
	'''
	'''
	
	import time

	status = {'red' : False, 'green' : False, 'blue' : False}  # TODO adapt for hardware
	
	def __init__(self, status=status):
		self.status = status
		
		self.on_activate()

	def on_activate(self):
		'''
		'''
		
	
		# Create I2C bus.
		self.i2c = busio.I2C(board.SCL, board.SDA)
	 
		# Create sensor instance.
		self.sensor = adafruit_vl6180x.VL6180X(self.i2c)

	def get_status(self):
		'''
		'''
		return self.status
		
	def get_range(self):
		'''
		'''
		range_mm = self.sensor.range
		return range_mm
		
	def get_lux(self):
		'''
		'''
		
		
		light_lux = self.sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)
		return light_lux
		
