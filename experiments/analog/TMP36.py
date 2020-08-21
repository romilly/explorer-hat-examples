import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    temperature = 100 * voltage
    print('temperature is %f4.1 degrees C' % temperature)
    sleep(1)
