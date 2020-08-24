import explorerhat as eh
from time import perf_counter, sleep

import RPi.GPIO as GPIO



TRAFFIC_RED = eh.light.red
TRAFFIC_AMBER = eh.light.yellow
TRAFFIC_GREEN = eh.light.green
PEDESTRIAN_WHITE = eh.output.one
PEDESTRIAN_RED = eh.output.two
PEDESTRIAN_GREEN = eh.output.three
LIGHTS = [TRAFFIC_RED, TRAFFIC_AMBER, TRAFFIC_GREEN,
          PEDESTRIAN_RED, PEDESTRIAN_GREEN]
MIN_GAP_DURATION = 20 # minimum seconds between crossing activations


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 50)
last_activation = perf_counter()-MIN_GAP_DURATION # se no delay if button is pressed immediately


def lights_off():
    for light in LIGHTS:
        light.off()


def beep(duration=0.2):
    buzzer.start(50)
    sleep(duration)
    buzzer.stop()
    sleep(1.0-duration)


def show(duration, *lights):
    lights_off()
    for light in lights:
        light.on()
    sleep(duration)


def run_pedestrian_cycle():
    show(1, TRAFFIC_AMBER, PEDESTRIAN_RED)
    show(1, TRAFFIC_RED, PEDESTRIAN_RED)
    PEDESTRIAN_WHITE.off()
    show(1, PEDESTRIAN_GREEN, TRAFFIC_RED)
    for i in range(10):
        if i in [6, 7, 8]:
            beep()
        if i == 9:
            beep(1.0)
    show(1, PEDESTRIAN_RED)
    show(1, TRAFFIC_GREEN)


def valid_pedestrian_request():
    global last_activation
    if eh.input.one.read():
        PEDESTRIAN_WHITE.on()
        while (perf_counter() < last_activation + MIN_GAP_DURATION):
            sleep(1)
        last_activation = perf_counter()
        return True
    else:
        return False


def run():
    while True:
        lights_off()
        TRAFFIC_GREEN.on()
        PEDESTRIAN_RED.on()
        if valid_pedestrian_request():
            run_pedestrian_cycle()





