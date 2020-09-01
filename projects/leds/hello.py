# blink the red LED on thr Explorer HAT
import explorerhat as eh
from time import sleep

eh.light.red.on()
sleep(2)
eh.light.red.off()
