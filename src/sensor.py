from datetime import datetime
from time import sleep

from pymemcache.client import base


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# GrovePi + Grove Ultrasonic Ranger

from grovepi import *

sensor1 = -1
timestamp1 = 0

sensor2 = -1
timestamp2 = 0

sensor3 = -1
timestamp3 = 0

sensor4 = -1
timestamp4 = 0


# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

def read_SonicSensor(ultrasonic_ranger):
    while True:
        try:
            # Read distance value from Ultrasonic
            lastValue = ultrasonicRead(ultrasonic_ranger)
            if (lastValue < 180 and lastValue > 1):
                print get_timestamp()
                print('sensor on port ' + str(ultrasonic_ranger) + ' :' + str(lastValue))
                sleep(0.8)
                return lastValue
            else:
                print "out of range sensor port " + ultrasonic_ranger

        except TypeError:
            pass
            # print "TypeError sensor port " + str(ultrasonic_ranger)
            # return "TypeError"
        except IOError:
            pass
            # print "IOError"
            # return "IOError"


# Create a handler for our read (GET) people
def read():
    print "sensor.read() called"
    while True:
        # sensor1 = read_SonicSensor(2)
        client = base.Client(('localhost', 11211))

        client.set('sensor4', read_SonicSensor(8))
        client.set('sensor4_timestamp', get_timestamp())

        client.set('sensor1', read_SonicSensor(7))
        client.set('sensor1_timestamp', get_timestamp())

        client.set('sensor2', read_SonicSensor(3))
        client.set('sensor2_timestamp', get_timestamp())

        client.set('sensor3', read_SonicSensor(4))
        client.set('sensor3_timestamp', get_timestamp())

        print "sensor values set to memcached"
        # sleep(1)
