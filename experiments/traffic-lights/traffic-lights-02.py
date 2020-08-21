import explorerhat as eh
from time import sleep

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 400)


RED = eh.light.red
GREEN = eh.light.green
ALL_LIGHTS = [RED, GREEN]

def beep():
    buzzer.start(50)
    sleep(0.2)
    buzzer.stop()
    sleep(0.8)


while True:
    eh.light.green.off()
    eh.light.red.on()
    if not eh.touch.one():
        continue
    sleep(1)
    eh.light.red.off()
    eh.light.green.on()
    for i in range(10):
        if i > 6:
            beep()


