from collections import namedtuple

import explorerhat
from time import sleep


RED = explorerhat.output.one
AMBER = explorerhat.output.two
GREEN = explorerhat.output.three
LIGHTS = [RED, AMBER, GREEN]

State = namedtuple('State', ['lights','duration', 'next'])

STATES = {
    'stop':     State([RED,], 5, 'ready'),
    'ready':    State([AMBER], 1, 'go'),
    'go':       State([GREEN], 5, 'caution'),
    'caution':  State([RED, AMBER], 1, 'stop')
}

state = STATES['stop']

while True:
    for light in LIGHTS:
        light.off()
    for light in state.lights:
        light.on()
    sleep(state.duration)
    state = STATES[state.next]




