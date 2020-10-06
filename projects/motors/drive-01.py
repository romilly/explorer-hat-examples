import explorerhat as eh
from time import sleep

for speed in range(10):
    eh.motor.one.forward(10*speed)
    sleep(1)
eh.motor.one.stop()
