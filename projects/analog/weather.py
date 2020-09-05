import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    centigrade = 100 * (voltage - 0.5)
    farenheit = 32 + 9 * centigrade / 5.0
    print('temperature is %4.1f degrees C or %4.1f degrees F'
          % (centigrade, farenheit))
    v2 = eh.analog.two.read()
    light = 'low'  if v2 > 3.5 else 'high'
    print('light level is %s' % light)
    sleep(1)
