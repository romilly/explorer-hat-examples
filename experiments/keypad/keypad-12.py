import explorerhat as eh
from time import sleep


def prepare_column(column):
    for each_col in range(3):
        if each_col == column:
            eh.output[each_col].off() # so it's at 5v
        else:
            eh.output[each_col].on()  # so it's at 0v


def check_for_key():
    while True:
        for col in range(3):
            prepare_column(col)
            for row in range(4):
                if eh.input[col].read():
                    return True, row, col
        return False, 0, 0


def key_pressed():
    pressed, row, col = False, 0, 0
    while not pressed:
        pressed, row, col = check_for_key()
    return pressed, row, col


def wait_for_release():
    while key_pressed()[0]:
        sleep(0.1)


while True:
    _, row, col = key_pressed()
    wait_for_release()
    print('row %d col %d pressed' % (row,col))
    sleep(0.1)
