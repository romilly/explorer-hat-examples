import explorerhat
from time import sleep

while True:
    if explorerhat.touch.three.is_pressed():
        explorerhat.light.red.on()
    else:
        explorerhat.light.red.off()
    sleep(0.1)
