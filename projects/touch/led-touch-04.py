import explorerhat as eh
from time import sleep


while True:
    for i in range(4):
        if eh.touch[i].is_pressed():
            eh.light[i].on()
        else:
            eh.light[i].off()
    sleep(0.1)
