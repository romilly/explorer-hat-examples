# blink the red LED on the Explorer HAT
import explorerhat as eh
from time import sleep

eh.light.red.on()
sleep(2)
eh.light.red.off()
