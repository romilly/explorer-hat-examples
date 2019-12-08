import explorerhat

while True:
    voltage = explorerhat.analog.one.read()
    print('voltage is %d V' % voltage)