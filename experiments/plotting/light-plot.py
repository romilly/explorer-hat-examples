import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    print((voltage,))
    sleep(1)


