import explorerhat

while True:
    voltage = explorerhat.analog.one.read()
    print('voltage is %f4.2 V' % voltage)
