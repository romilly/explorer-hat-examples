import explorerhat
from time import sleep


while True:
    if explorerhat.touch.one.is_pressed():
        explorerhat.output.one.on()
    else:
        explorerhat.output.one.off()
    sleep(0.1)

