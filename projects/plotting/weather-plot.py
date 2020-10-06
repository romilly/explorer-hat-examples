import explorerhat as eh
from time import sleep
from math import log

def lux(resistance):
   return 300 * (3.0**-log(resistance/3000.0, 2))

r1 = 10000
delay = 1 # for testing
# delay = 600 # every 10 minutes, for production use!

while True:
    v1 = eh.analog.one.read()
    celsius = 100.0 * (v1 - 0.5)
    v2 = eh.analog.two.read()
    ldr = r1 * v2 / (5 - v2)
    level = lux(ldr)
    print((celsius, level))
    sleep(delay)
