import explorerhat as eh
from time import sleep


while True:
    v2 = eh.analog.two.read()
    light_level = 1000 * v2 / (5 - v2)
    print('light level is %4.1f' % light_level)
    sleep(1)
