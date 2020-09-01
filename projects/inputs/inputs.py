import explorerhat as hat
from time import sleep

while True:
    if hat.input.one.read():
        print('oooh')
    sleep(0.25)