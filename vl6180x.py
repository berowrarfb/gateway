import time
import board
import busio
import adafruit_vl6180x
import adafruit_vl6180x

class sensor_vl6180x():
	''' For the Adafruit vl6180x time-of-flight 
		range sensor.
	'''
	
	def __init__(self):
		'''
		'''
		
		self.on_activate()

	def on_activate(self):
		''' Init the device hardware
		'''
	
		# Create I2C bus.
		self.i2c = busio.I2C(board.SCL, board.SDA)
	 
		# Create sensor instance.
		self.sensor = adafruit_vl6180x.VL6180X(self.i2c)
		
	def get_range(self):
		''' Return the range in mm
		'''
		range_mm = self.sensor.range
		return range_mm
		
	def get_lux(self):
		''' Return the lux in ???
		'''
		
		light_lux = self.sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)
		return light_lux
		
