import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    centigrade = 100 * (voltage - 0.5)
    farenheit = 32 + 9 * centigrade / 5.0
    print('temperature is %4.1f degrees C or %4.1f degrees F'
          % (centigrade, farenheit))
    sleep(1)
