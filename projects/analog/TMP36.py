import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    celsius = 100 * (voltage - 0.5)
    fahrenheit = 32 + 9 * celsius / 5.0
    print('Temperature is %4.1f degrees C or %4.1f degrees F'
          % (celsius, fahrenheit))
    sleep(1)
