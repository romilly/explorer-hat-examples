import explorerhat as eh
from time import sleep

MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '-': '-....-',
    '/': '-..-.',
    ':': '---...',
    '\'': '.----.',
    ')': '-.--.-',
    ';': '-.-.-',
    '(': '-.--.',
    '=': '-...-',
    '@': '.--.-.',
}

LENGTHS = { '.' : 1, '-': 3}

UNIT_DURATION = 0.2

def flash(length, value):
    if value == 0:
        eh.light.red.off()
        sleep(length * UNIT_DURATION)
        return
    eh.light.red.on()
    sleep(length * UNIT_DURATION)



def morse(text, send):
    for word in text.split():
        for ch in word:
            for m in MORSE_CODE[ch]:
                send(LENGTHS[m], 1)
                send(1, 0)
            send(2, 0)
        send(4,0)

morse('SOS', flash)

