from datetime import datetime
from time import sleep

from grovepi import *
from pymemcache.client import base

import properties

"""
This function returns the current time as a timestamp 
 
:return: current formatted time
"""


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
# Ignore errors, since that is normal behaviour when using multiple sonics sensors on a single grovepi.

"""
This function returns the sensor value of sonic sensor in cm. 
 
:param: number of digital port of grovepi where the sonic sensor is connected
:return: distance in cm of requested digital port
"""


def read_SonicSensor(ultrasonic_ranger):
    while True:
        try:
            # Read distance value from Ultrasonic
            last_value = ultrasonicRead(ultrasonic_ranger)
            if 180 > last_value > 1:
                print get_timestamp()
                print('sensor on port ' + str(ultrasonic_ranger) + ' :' + str(last_value))
                sleep(0.8)  # absolutely essential to avoid overwriting sensor data
                return last_value
                # else:
                #     print('out of range sensor on port ' + str(ultrasonic_ranger) + ' :' + str(last_value))

        except TypeError:
            pass  # ignore
            # print "TypeError sensor port " + str(ultrasonic_ranger)
        except IOError:
            pass
            # print "IOError sensor port " + str(ultrasonic_ranger)


"""
This function reads the distance for each sonic sensor and stores the values in memcache.
"""


def cyclic_read_distances():
    while True:
        client = base.Client((properties.memcacheHost, properties.memcachePort))

        client.set('sensor4', read_SonicSensor(8))
        client.set('sensor4_timestamp', get_timestamp())

        client.set('sensor1', read_SonicSensor(7))
        client.set('sensor1_timestamp', get_timestamp())

        client.set('sensor2', read_SonicSensor(3))
        client.set('sensor2_timestamp', get_timestamp())

        client.set('sensor3', read_SonicSensor(4))
        client.set('sensor3_timestamp', get_timestamp())

        print "sensor values set to memcached"
