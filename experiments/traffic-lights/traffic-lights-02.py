import explorerhat as eh
from time import sleep

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 400)


RED = eh.light.red
GREEN = eh.light.green
ALL_LIGHTS = [RED, GREEN]


def beep(duration=0.2):
    buzzer.start(50)
    sleep(duration)
    buzzer.stop()
    sleep(1.0-duration)


while True:
    eh.light.green.off()
    eh.light.red.on()
    if not eh.touch.one.is_pressed():
        continue
    sleep(1)
    eh.light.red.off()
    eh.light.green.on()
    for i in range(10):
        if i in [6, 7, 8]:
            beep()
        if i == 9:
            beep(1.0)



