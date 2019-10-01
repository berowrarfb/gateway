import kit11588
import vl6180x

leds = kit11588.led_breakout_kit11588()
range_device = vl6180x.sensor_vl6180x()

run = True

try:
    while True:
        range = range_device.get_range()

        if 0 <= range <= 100:
            leds.set_led({'red':True, 'green':False, 'blue':False})
        elif 100 <= range <= 200:
            leds.set_led({'red':False, 'green':True, 'blue':False})
        else:
            leds.set_led({'red':False, 'green':False, 'blue':True})
except:
    leds.set_led({'all':False})
