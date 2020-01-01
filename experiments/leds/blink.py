import explorerhat as eh
from time import sleep

while True:
    eh.light.red.on()
    sleep(1)
    eh.light.red.off()
    sleep(1)
