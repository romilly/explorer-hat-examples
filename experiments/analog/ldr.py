import explorerhat as eh
from time import sleep

while True:
    voltage = eh.analog.one.read()
    print('voltage is %f4.2 V' % voltage)
    # if voltage > 2.5:
    #     eh.light.red.on()
    #     eh.light.green.off()
    # else:
    #     eh.light.red.off()
    #     eh.light.green.on()
    sleep(0.1)


