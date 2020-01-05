import explorerhat
from time import sleep

while True:
    explorerhat.light.red.off()
    if explorerhat.touch.three.is_pressed():
        explorerhat.light.red.on()
    sleep(0.1)
