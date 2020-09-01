import explorerhat as eh
from time import sleep

while True:
    eh.output.one.on()
    sleep(1)
    eh.output.one.off()
    sleep(1)
