import explorerhat
from time import sleep


while True:
    for i in range(4):
        if explorerhat.touch[i].is_pressed():
            explorerhat.light[i].on()
        else:
            explorerhat.light[i].off()
    sleep(0.1)
