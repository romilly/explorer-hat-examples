import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    print('Voltage is %4.1f V' % voltage)
    sleep(1)
