import explorerhat
from time import sleep


while True:
    if explorerhat.touch.one.is_pressed():
        explorerhat.output.one.on()
    else:
        explorerhat.output.one.off()
    if explorerhat.touch.two.is_pressed():
        explorerhat.output.two.on()
    else:
        explorerhat.output.two.off()
    if explorerhat.touch.three.is_pressed():
        explorerhat.output.three.on()
    else:
        explorerhat.output.three.off()
    sleep(0.1)

