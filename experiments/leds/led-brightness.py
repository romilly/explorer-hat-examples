import explorerhat
from time import sleep

while True:
    pc = 0
    for i in range(10):
        explorerhat.light.red.brightness(pc)
        pc += 10
        sleep(0.1)
