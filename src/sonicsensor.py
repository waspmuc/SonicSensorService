from datetime import datetime
from time import sleep
import sensor
from pymemcache.client import base
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# GrovePi + Grove Ultrasonic Ranger

from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

def read_SonicSensor(ultrasonic_ranger):

   while True:
      try:
           # Read distance value from Ultrasonic
           lastValue = ultrasonicRead(ultrasonic_ranger)
           if(lastValue < 200 and lastValue > 3):
              print get_timestamp()
              print lastValue
	      sleep(0.25)
	      return lastValue
           else:
              print "out of range"

      except TypeError:
          print "Error"
          return "Error"
      except IOError:
          print "Error"
          return "Error"

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """

    client = base.Client(('localhost', 11211))
    print "accessing memcache"

    RESPONSE = {
 	 "Sensor1": {
  	    "distance": client.get('sensor1'),
  	    "timestamp": client.get('sensor1_timestamp')
         },
         "Sensor2": {
            "distance": client.get('sensor2'),
            "timestamp": client.get('sensor2_timestamp')
         },
         "Sensor3": {
            "distance": client.get('sensor3'),
            "timestamp": client.get('sensor3_timestamp')
         },
         "Sensor4": {
            "distance": client.get('sensor4'),
            "timestamp": client.get('sensor4_timestamp')
         }
    }

    # Create the list of people from our data
    #return [RESPONSE[key] for key in sorted(RESPONSE.keys())]
    return RESPONSE
