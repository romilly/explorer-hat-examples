import explorerhat
from time import sleep


while True:
    explorerhat.light.off()
    if explorerhat.touch.one.is_pressed():
        explorerhat.light.blue.on()
    if explorerhat.touch.two.is_pressed():
        explorerhat.light.yellow.on()
    if explorerhat.touch.three.is_pressed():
        explorerhat.light.red.on()
    if explorerhat.touch.four.is_pressed():
        explorerhat.light.green.on()
    sleep(0.1)
