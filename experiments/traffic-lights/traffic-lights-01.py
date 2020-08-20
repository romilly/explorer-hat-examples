import explorerhat as eh
from time import sleep


RED = eh.light.red
AMBER = eh.light.yellow
GREEN = eh.light.green
ALL_LIGHTS = [RED, AMBER, GREEN]

def show(duration, lights):
    for light in ALL_LIGHTS:
        light.off()
    for light in lights:
        light.on()
    sleep(duration)


while True:
    show(5, [RED])
    show(1, [AMBER])
    show(5,[GREEN])
    show(1, [RED, AMBER])





