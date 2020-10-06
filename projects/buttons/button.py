import explorerhat as eh
from time import sleep

while True:
    if eh.input.one.read():
        eh.light.red.on()
    else:
        eh.light.red.off()
    sleep(0.1)
