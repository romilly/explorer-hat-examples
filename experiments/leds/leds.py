import explorerhat as eh
from time import sleep


while True:
    eh.light.off()
    eh.light.red.on()
    sleep(0.5)
    eh.light.yellow.on()
    sleep(0.5)
    eh.light.green.on()
    sleep(0.5)
    eh.light.blue.on()
    sleep(0.5)
