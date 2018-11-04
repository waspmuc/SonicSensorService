from datetime import datetime

from pymemcache.client import base


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

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
    # return [RESPONSE[key] for key in sorted(RESPONSE.keys())]
    return RESPONSE
