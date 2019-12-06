import explorerhat
from time import sleep


while True:
    explorerhat.output.one.on()
    sleep(1)
    explorerhat.output.one.off()
    sleep(1)
