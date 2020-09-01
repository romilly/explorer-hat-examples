import explorerhat as eh
from time import sleep

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 50)


RED = eh.light.red
GREEN = eh.light.green
ALL_LIGHTS = [RED, GREEN]


def beep(duration=0.2):
    buzzer.start(50)
    sleep(duration)
    buzzer.stop()
    sleep(1.0-duration)


while True:
    GREEN.off()
    RED.on()
    if not eh.touch.one.is_pressed():
        continue
    sleep(1)
    RED.off()
    GREEN.on()
    for i in range(10):
        if i in [6, 7, 8]:
            beep()
        if i == 9:
            beep(1.0)



