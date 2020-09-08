import explorerhat as eh
from time import sleep


while True:
    v2 = eh.analog.two.read()
    r1 = 10000
    light_level = r1 * v2 / (5 - v2)
    print('v2 is %4.1f andlight level is %4.1f' % (v2, light_level))
    sleep(1)
