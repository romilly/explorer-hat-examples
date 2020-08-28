import explorerhat as eh
from time import sleep


MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '-': '-....-',
    '/': '-..-.', ':': '---...', '\'': '.----.', ')': '-.--.-',
    ';': '-.-.-', '(': '-.--.', '=': '-...-','@': '.--.-.',
}

LENGTHS = {'.': 1, '-': 3}
UNIT_DURATION = 0.2
ON = 1
OFF = 0


def flash(length, value):
    if value == OFF:
        eh.light.red.off()
    else:
        eh.light.red.on()
    sleep(length * UNIT_DURATION)


def morse(text):
    for word in text.split():
        for ch in word:
            for m in MORSE_CODE[ch]:
                flash(LENGTHS[m], ON)
                flash(1, OFF)
            flash(2, OFF)
        flash(4, OFF)


morse('SOS')
