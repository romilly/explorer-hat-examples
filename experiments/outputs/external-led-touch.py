import explorerhat as eh
from time import sleep


while True:
    if eh.touch.three.is_pressed():
        eh.output.one.on()
    else:
        eh.output.one.off()
    sleep(0.1)
