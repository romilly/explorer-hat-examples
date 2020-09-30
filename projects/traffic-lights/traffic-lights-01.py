import explorerhat as eh
from time import sleep

# Name the built-in lights so the code below is more readable.
RED = eh.light.red
AMBER = eh.light.yellow
GREEN = eh.light.green
ALL_LIGHTS = [RED, AMBER, GREEN]


def show(duration, *lights):
    for current_light in ALL_LIGHTS:
        if current_light in lights:
            current_light.on()
        else:
            current_light.off()
    sleep(duration)


while True:
    show(5, RED)
    show(1, RED, AMBER)
    show(5, GREEN)
    show(1, AMBER)








