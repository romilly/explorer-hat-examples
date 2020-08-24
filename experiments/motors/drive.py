import explorerhat as eh

for speed in range(10):
    eh.motor.one.forward(10*speed)
eh.motor.one.stop()