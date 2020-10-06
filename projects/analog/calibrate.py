import explorerhat as eh
from time import sleep


while True:
    v2 = eh.analog.two.read()
    r1 = 10000
    ldr = r1 * v2 / (5 - v2)
    print('v2 is %4.1f and LDR is %4.1f ohms' % (v2, ldr))
    sleep(1)
