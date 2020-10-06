import explorerhat as eh
from time import sleep

while True:
    v1 = eh.analog.one.read()
    celsius = 100.0 * (v1 - 0.5)
    fahrenheit = 32 + 9 * celsius / 5.0
    print('Temperature is %4.1f degrees C or %4.1f degrees F'
          % (celsius, fahrenheit))
    v2 = eh.analog.two.read()
    light_level = 'low' if v2 > 3.5 else 'high'
    print('Light level is %s' % light_level)
    sleep(1)
