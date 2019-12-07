import explorerhat as hat
from time import sleep


while True:
    hat.light.off()
    hat.light.red.on()
    sleep(0.5)
    hat.light.yellow.on()
    sleep(0.5)
    hat.light.green.on()
    sleep(0.5)
    hat.light.blue.on()
    sleep(0.5)
