import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    print('voltage is %4.2f V' % voltage)
    sleep(1)
