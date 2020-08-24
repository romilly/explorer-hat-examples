import explorerhat as eh
from time import sleep

while True:
    if eh.touch.one.is_pressed():
        eh.motor.one.forward(100)
        sleep(0.1)
        continue
    if eh.touch.two.is_pressed():
        eh.motor.one.backward(100)
        sleep(0.1)
