import explorerhat
from time import sleep


RED = explorerhat.output.one
YELLOW = explorerhat.output.two
GREEN = explorerhat.output.three


while True:
    if explorerhat.touch.one.is_pressed():
        RED.on()
    else:
        RED.off()
    if explorerhat.touch.two.is_pressed():
        YELLOW.on()
    else:
        YELLOW.off()
    if explorerhat.touch.three.is_pressed():
        GREEN.on()
    else:
        GREEN.off()
    sleep(0.1)

