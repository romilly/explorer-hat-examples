"""Simulates a single UK traffic light

Requires a Raspberry Pi and a Pimoroni Explorer Hat.

To learn more about this and other Explorer Hat examples,
get 'Explorer Hat Tricks', available from Leanpub
at https://leanpub.com/explorerhattricks
"""

import explorerhat as eh
from time import sleep

# Name the built-in lights so the code below is more readable.
RED = eh.light.red
AMBER = eh.light.yellow
GREEN = eh.light.green
ALL_LIGHTS = [RED, AMBER, GREEN]


def show(duration, *lights):
    """Turns on the specified LEDs, then waits for <duration>.

    Lights not in the list of required lights will be turned off

    Args:
        duration: # of seconds to sleep after lights are turned on.
        lights: a list of Explorer Hat LEDs to be turned on.
    """
    for light in ALL_LIGHTS:
        if light in lights:
            light.on()
        else:
            light.off()
    sleep(duration)


while True:
    show(5, RED)
    show(1, RED, AMBER)
    show(5, GREEN)
    show(1, RED)







