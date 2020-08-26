"""Simulates a single UK traffic light

Requires a Raspberry Pi and a Pimoroni Explorer Hat.

To learn more about this and other Explorer Hat examples, get 'Explorer Hat Tricks',
available from Leanpub https://leanpub.com/explorerhattricks
"""

import explorerhat as eh
from time import sleep

# Name the built-in lights so the code below is more readable.
RED = eh.light.red
AMBER = eh.light.yellow
GREEN = eh.light.green
ALL_LIGHTS = [RED, AMBER, GREEN]


def show(duration, lights):
    """Turns on the specified HAT's built-in lights and waits for a given length of time.

    Lights not in the list will be turned off

    Args:
        duration: length of time to sleep after lights have been turned on.
        lights: a list of Explorer Hat light objects to be turned on.
    """
    for light in ALL_LIGHTS:
        if light in lights:
            light.on()
        else:
            light.off()
    sleep(duration)


def run():
    """Loop forever displaying the lights in sequence."""
    while True:
        show(5, [RED])
        show(1, [RED, AMBER])
        show(5,[GREEN])
        show(1, [RED])


run()





