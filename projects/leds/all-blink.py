import explorerhat as eh
from time import sleep

for i in range(10):
    eh.light.blue.on()
    sleep(0.1)
    eh.light.yellow.on()
    sleep(0.1)
    eh.light.red.on()
    sleep(0.1)
    eh.light.green.on()
    sleep(0.1)
    eh.light.off()
    sleep(0.1)
print('Time to stop!')