import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    print('voltage is %f4.2 V' % voltage)
    sleep(1)
