from pymemcache.client import base

import properties


def read_sensorvalues_from_cache():
    """
    This function responds to a request for /api/sonicsensor

    :return: all sensor values and timestamp
    """

    client = base.Client((properties.memcacheHost, properties.memcachePort))

    response = [{
        "Sensor1": {
            "distance": int(client.get('sensor1')),
            "timestamp": client.get('sensor1_timestamp')
        },
        "Sensor2": {
            "distance": int(client.get('sensor2')),
            "timestamp": client.get('sensor2_timestamp')
        },
        "Sensor3": {
            "distance": int(client.get('sensor3')),
            "timestamp": client.get('sensor3_timestamp')
        },
        "Sensor4": {
            "distance": int(client.get('sensor4')),
            "timestamp": client.get('sensor4_timestamp')
        }
    }]

    return response
