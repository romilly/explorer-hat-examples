import explorerhat as eh
from time import sleep

CHAR_TABLE = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]


def prepare_column(column):
    for each_col in range(3):
        if each_col == column:
            eh.output[each_col].off() # so it's at 5v
        else:
            eh.output[each_col].on()  # so it's at 0v


def all_columns_on():
    for col in range(3):
        eh.output[col].on()


def check_for_key():
    while True:
        for col in range(3):
            prepare_column(col)
            for row in range(4):
                sleep(0.01)
                if eh.input[row].read():
                    all_columns_on()
                    return True, row, col
        all_columns_on()
        return False, 0, 0


def key_pressed():
    pressed, row, col = False, 0, 0
    while not pressed:
        pressed, row, col = check_for_key()
    return pressed, row, col


def wait_for_release():
    while check_for_key()[0]:
        sleep(0.1)


def decode_key(prc,table):
    p, row, col = prc
    return table[row][col]


while True:
    ch = decode_key(key_pressed(), CHAR_TABLE)
    print('%s pressed' % ch)
    wait_for_release()
    sleep(0.1)
